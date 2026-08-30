# Week 1 Practice: Python Basics
# Goal: Practice lists, loops, and if statements.

# TODO 1: Create a list of your favorite Azure services (at least 3).
# Example: my_services = ["Azure Functions", "Azure Storage"]
azure_services = ["Azure Functions", "Azure Storage", "Azure OpenAI"]

# TODO 2: Use a 'for' loop to print each service in your list.
# Write your loop below:
for service in azure_services:
    print(f"Service: {service}")

# TODO 3: Use an 'if' statement to check if "Azure OpenAI" is in the list. 
# If it is, print a special message like "GenAI is the future!"
# Write your if statement below:
if "Azure OpenAI" in azure_services:
    print("GenAI is the future!")

# Bonus: Try adding a new service to the list using the .append() method
# and print the list again.
azure_services.append("Azure AI Search")
print(f"Updated list: {azure_services}")
