# Week 1 Practice: Python Functions
# Goal: Practice defining and calling functions, passing arguments, and returning values.

# TODO 1: Write a function called `greet_user` that takes a name (string) as an argument
# and prints a personalized greeting (e.g., "Hello, Akash! Welcome to Azure.")
# Write your function below:
def greet_user(name):
    print(f"Hello, {name}! Welcome to Azure.")

# TODO 2: Call the `greet_user` function you just wrote, passing in your own name.
greet_user("Akash")

# TODO 3: Write a function called `calculate_cost` that takes two arguments:
# - hours (number)
# - hourly_rate (number)
# The function should RETURN the total cost (hours * hourly_rate).
# Write your function below:
def calculate_cost(hours, hourly_rate):
    return hours * hourly_rate

# TODO 4: Call `calculate_cost`, save the result in a variable, and print it out.
# Example: total = calculate_cost(5, 10)
#          print(f"Total cost: ${total}")
total = calculate_cost(5, 10)
print(f"Total cost: ${total}")
