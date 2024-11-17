def add_expense(expenses):
    item = input("Enter the item name: ")
    cost = float(input(f"Enter the cost of {item}: "))
    expenses[item] = cost
    print(f"{item} added with cost {cost}.")

def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
    else:
        print("\nExpenses List:")
        total = 0
        for item, cost in expenses.items():
            print(f"{item}: ${cost}")
            total += cost
        print(f"Total Expenses: ${total}")

def expense_tracker():
    expenses = {}
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Exiting Expense Tracker!")
            break
        else:
            print("Invalid choice!")

# Run the tracker
if __name__ == "__main__":
    expense_tracker()