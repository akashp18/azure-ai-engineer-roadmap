# Part 2 Advanced Milestone Project: Async Weather & API Client
# Goal: Combine OOP, Async/Await, Env Vars, Error Handling, and Type Hinting!

import os
import asyncio
import time
from dotenv import load_dotenv

# We will use `aiohttp` for asynchronous HTTP requests. 
# (You may need to run `pip install aiohttp` in your terminal).
import aiohttp

load_dotenv()

# TODO 1: Define a `WeatherClient` class.
class WeatherClient:
    
    # TODO 2: Create the __init__ method. Use type hinting (-> None).
    # It should read 'AZURE_OPENAI_KEY' from os.getenv(). 
    # If the key is not found, raise a ValueError("API Key is missing!").
    # We won't actually use this key for the free weather API, but this is great practice!
    def __init__(self) -> None:
        self.api_key = os.getenv('AZURE_OPENAI_KEY')
        if not self.api_key:
            raise ValueError("API Key is missing!")
        
    # TODO 3: Create an async method `fetch_weather` that takes `self` and `city: str`.
    # It should return a `dict` (Type Hinting: -> dict).
    async def fetch_weather(self, city: str) -> dict:
        # We will use the free Open-Meteo API (no key required) just to test async requests.
        # Here are the coordinates for 3 cities:
        locations = {
            "New York": "latitude=40.71&longitude=-74.01",
            "London": "latitude=51.51&longitude=-0.13",
            "Tokyo": "latitude=35.69&longitude=139.69"
        }
        
        # If the city isn't in our dictionary, default to New York.
        coords = locations.get(city, locations["New York"])
        url = f"https://api.open-meteo.com/v1/forecast?{coords}&current_weather=true"
        
        # TODO 4: Use `aiohttp.ClientSession()` to make a GET request to the URL.
        # Wrap it in a `try...except` block to catch `aiohttp.ClientError`.
        # Write your code here:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    temp = data['current_weather']['temperature']
                    print(f"Weather in {city}: {temp}°C")
                    return data
        except aiohttp.ClientError as e:
            print(f"Network error while fetching weather for {city}: {e}")
            return {}

# TODO 5: Create an async `main() -> None` function.
# Inside, create an instance of `WeatherClient`. 
# Then use `asyncio.gather()` to fetch the weather for "New York", "London", and "Tokyo" concurrently!
async def main() -> None:
    try:
        client = WeatherClient()
    except ValueError as e:
        print(f"Error starting client: {e}")
        return

    print("Fetching weather concurrently...\n")
    start_time = time.time()
    
    await asyncio.gather(
        client.fetch_weather("New York"),
        client.fetch_weather("London"),
        client.fetch_weather("Tokyo")
    )
    
    print(f"\nAll fetches completed in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    # Run the main async loop
    asyncio.run(main())
