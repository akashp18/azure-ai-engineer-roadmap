# Part 2 Advanced Milestone Project: Interactive Async Weather CLI
# Goal: Combine OOP, Async/Await, Env Vars, Error Handling, and Type Hinting!

import os
import asyncio
import time
from dotenv import load_dotenv
import aiohttp

load_dotenv()

class WeatherClient:
    
    def __init__(self) -> None:
        self.api_key = os.getenv('AZURE_OPENAI_KEY')
        if not self.api_key:
            raise ValueError("API Key is missing!")
            
    async def fetch_spell_check(self, query: str) -> list[str]:
        """Uses Datamuse API to find spelling suggestions for misspelled cities."""
        url = f"https://api.datamuse.com/words?sp={query}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    # Return top 3 suggestions
                    return [item['word'].title() for item in data[:3]]
        except aiohttp.ClientError:
            return []
            
    async def fetch_coordinates(self, query: str) -> list[dict]:
        """Fetches coordinates for a given city name using Open-Meteo Geocoding API."""
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={query}&count=10&language=en&format=json"
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    return data.get("results", [])
        except aiohttp.ClientError as e:
            print(f"Network error while fetching coordinates for {query}: {e}")
            return []

    async def fetch_weather(self, lat: float, lon: float, location_name: str) -> dict:
        """Fetches the current weather for exact coordinates."""
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    temp = data['current_weather']['temperature']
                    print(f"\n🌤️  Weather in {location_name}: {temp}°C\n")
                    return data
        except aiohttp.ClientError as e:
            print(f"Network error while fetching weather for {location_name}: {e}")
            return {}

async def main() -> None:
    try:
        client = WeatherClient()
    except ValueError as e:
        print(f"Error starting client: {e}")
        return

    print("=== Welcome to the Intelligent Weather CLI ===")
    print("Type 'quit' to exit.")

    while True:
        city = input("\nEnter a city name: ").strip()
        
        if city.lower() == 'quit':
            print("Goodbye!")
            break
            
        if not city:
            continue
            
        print(f"Searching for '{city}'...")
        results = await client.fetch_coordinates(city)
        
        # INTELLIGENT FALLBACK: If no results found, try spell check!
        if not results:
            suggestions = await client.fetch_spell_check(city)
            if suggestions:
                print(f"❌ Could not find '{city}'. Did you mean:")
                for idx, sugg in enumerate(suggestions):
                    print(f"  {idx + 1}) {sugg}")
                
                selection = input("\nEnter the number of the correct city (or 'c' to cancel): ").strip()
                if selection.lower() == 'c':
                    continue
                    
                try:
                    sel_idx = int(selection) - 1
                    if 0 <= sel_idx < len(suggestions):
                        city = suggestions[sel_idx]
                        print(f"\nSearching for corrected city: '{city}'...")
                        results = await client.fetch_coordinates(city)
                        if not results:
                            print(f"❌ Could not find coordinates for '{city}' either. Please try a major city.")
                            continue
                    else:
                        print("❌ Invalid selection.")
                        continue
                except ValueError:
                    print("❌ Please enter a valid number.")
                    continue
            else:
                print(f"❌ Could not find any cities matching '{city}' and no spelling suggestions were found.")
                continue
            
        # If exactly one result is found, fetch weather immediately
        if len(results) == 1:
            location = results[0]
            name = f"{location.get('name')}, {location.get('admin1', '')} {location.get('country', '')}".strip(', ')
            await client.fetch_weather(location['latitude'], location['longitude'], name)
            continue
            
        # If multiple results are found, ask the user to clarify
        print(f"\nFound {len(results)} matches for '{city}'. Did you mean:")
        for idx, loc in enumerate(results):
            name = loc.get('name')
            admin1 = loc.get('admin1', 'N/A')
            country = loc.get('country', 'N/A')
            print(f"  {idx + 1}) {name}, {admin1}, {country}")
            
        selection = input("\nEnter the number of the correct city (or 'c' to cancel): ").strip()
        
        if selection.lower() == 'c':
            continue
            
        try:
            sel_idx = int(selection) - 1
            if 0 <= sel_idx < len(results):
                location = results[sel_idx]
                name = f"{location.get('name')}, {location.get('admin1', '')} {location.get('country', '')}".strip(', ')
                await client.fetch_weather(location['latitude'], location['longitude'], name)
            else:
                print("❌ Invalid selection.")
        except ValueError:
            print("❌ Please enter a valid number.")

if __name__ == "__main__":
    asyncio.run(main())
