# Week 2 Practice: Asynchronous Programming (async / await)
# Goal: Write an asynchronous function to simulate making multiple API calls at the same time.

import asyncio
import time

# TODO 1: Define an asynchronous function called `fetch_data` that takes an argument `item_id`.
# Hint: Use `async def`
# Write your code below:
async def fetch_data(item_id):


    # TODO 2: Inside the function, print a message like: f"Fetching data for item {item_id}..."
    # Write your code below:
    print(f"Fetching data for item {item_id}...")
    

    # TODO 3: Simulate a network delay by using `await asyncio.sleep(2)`.
    # Write your code below:
    await asyncio.sleep(2)
    

    # TODO 4: Print a message indicating the fetch is complete, like: f"Finished fetching item {item_id}"
    # Write your code below:
    print(f"Finished fetching item {item_id}")
    

# TODO 5: Define the main async function to run everything.
# We'll use asyncio.gather to run 3 tasks concurrently.
async def main():
    start_time = time.time()
    
    # Run fetch_data(1), fetch_data(2), and fetch_data(3) at the same time:
    print("Starting concurrent API calls...")
    
    # Write your code using await asyncio.gather(...) below:
    await asyncio.gather(
        fetch_data(1),
        fetch_data(2),
        fetch_data(3)
    )
    
    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")

# Run the async main loop
if __name__ == "__main__":
    asyncio.run(main())
