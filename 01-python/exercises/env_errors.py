# Week 2 Practice: Environment Variables & Error Handling
# Goal: Use `python-dotenv` to load a fake API key, and use try/except to handle network errors.

import os
import requests
from dotenv import load_dotenv

# TODO 1: Load the environment variables from the `.env` file using load_dotenv().
# Write your code below:
load_dotenv()


# TODO 2: Get the 'AZURE_OPENAI_KEY' from the environment variables using os.getenv().
# Save it to a variable called `api_key`.
# Write your code below:
api_key = os.getenv("AZURE_OPENAI_KEY")


# TODO 3: Check if the api_key exists using an if statement. 
# If it doesn't, print a warning.
# Otherwise, print a success message (but don't print the actual key for security!)
# Write your code below:
if api_key:
    print("Success: Azure API Key found securely!")
else:
    print("Warning: AZURE_OPENAI_KEY not found in .env file.")


# TODO 4: We are going to make a request to a URL that takes too long to respond.
# This will intentionally trigger a timeout error.
# Wrap the following 2 lines of code in a `try` block, and catch the `requests.exceptions.Timeout` error!

# fake_url = "https://httpbin.org/delay/5"
# response = requests.get(fake_url, timeout=2)

# Write your try/except block below:
try:
    fake_url = "https://httpbin.org/delay/5"
    print(f"\nCalling API at {fake_url}...")
    response = requests.get(fake_url, timeout=2)
except requests.exceptions.Timeout:
    print("Error: The API request timed out! This is expected.")

