# Week 1 Practice: JSON & APIs
# Goal: Practice using the `requests` library to fetch data from an API, and parse JSON.

import requests
import json

# TODO 1: Make a GET request to a public API. Let's use the GitHub API to get your user info.
# Replace 'YOUR_GITHUB_USERNAME' with your actual username (e.g. 'akashpatel95' based on your link earlier).
github_username = "akashpatel95"
url = f"https://api.github.com/users/{github_username}"

# Use requests.get(url) to fetch the data and save it to a variable called `response`.
# Write your code below:
response = requests.get(url)


# TODO 2: Check if the request was successful by printing the status code (response.status_code).
# It should be 200.
# Write your code below:
print(f"Status Code: {response.status_code}")


# TODO 3: Parse the JSON data from the response. 
# Use response.json() and save it to a variable called `data`.
# Write your code below:
data = response.json()


# TODO 4: Print out specific pieces of information from the JSON dictionary.
# For example, print your 'name', 'public_repos', and 'followers'.
# Write your code below:
print(f"Name: {data.get('name')}")
print(f"Public Repos: {data.get('public_repos')}")
print(f"Followers: {data.get('followers')}")
