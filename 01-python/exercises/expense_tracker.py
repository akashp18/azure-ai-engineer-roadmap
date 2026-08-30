# Week 1 Milestone Project: Expense Tracker CLI
# Goal: Build a command-line application that tracks expenses using a list of dictionaries.

def main():
    expenses = []
    print("Welcome to the Expense Tracker!")
    print("Type 'quit' at any time to exit and see your total.\n")

    while True:
        # TODO 1: Ask the user for the name of the expense (e.g., 'Coffee'). 
        # Use the input() function.
        # If they type 'quit', break out of the loop.
        # Write your code below:
        expense_name = input("Enter expense name (or 'quit' to exit): ")
        if expense_name.lower() == 'quit':
            break
        
        # TODO 2: Ask the user for the amount (e.g., '5.50'). 
        # Make sure to convert this input from a string to a float!
        # Write your code below:
        try:
            expense_amount = float(input("Enter amount: $"))
        except ValueError:
            print("Invalid amount. Please enter a number.\n")
            continue
        
        # TODO 3: Create a dictionary for this expense with keys 'name' and 'amount',
        # and append it to the `expenses` list.
        # Write your code below:
        expense = {"name": expense_name, "amount": expense_amount}
        expenses.append(expense)
        
        print("Expense added successfully!\n")

    # --- After the loop (when the user types 'quit') ---
    print("\n--- Your Expenses ---")
    
    # TODO 4: Loop through the `expenses` list and print each expense.
    # Also, calculate the total sum of all expenses and print the grand total.
    # Write your code below:
    total = 0.0
    for exp in expenses:
        print(f"- {exp['name']}: ${exp['amount']:.2f}")
        total += exp['amount']
    
    print(f"\nGrand Total: ${total:.2f}")
    
    

if __name__ == "__main__":
    main()
