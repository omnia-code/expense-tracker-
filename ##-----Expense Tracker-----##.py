##-----Expense Tracker-----##
Expenses = []

print("Welcome to the Expense Tracker!")

while True:
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense_name = input("Enter the name of the expense: ")
        expense_amount = float(input("Enter the amount of the expense: "))
        Expenses.append((expense_name, expense_amount))
        print("Expense added successfully!") 

    
    elif choice == "2":
        if Expenses:
            for expense_name, expense_amount in Expenses:
                print(f"{expense_name}: {expense_amount}")
        else:
            print("No expenses recorded.")
    elif choice == "3":
        total = sum(expense_amount for _, expense_amount in Expenses)
        print(f"Total expenses: {total}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")