from datetime import datetime

def add_expense(expenses, amount, date):
    category = choose_category()
    expense = {'amount': amount, 'category': category, 'date': date}
    expenses.append(expense)
    save_expenses_to_file(expenses)

def print_expenses(expenses):
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. Amount: {expense['amount']}, Category: {expense['category']}, Date: {expense['date']}")

def total_expenses(expenses):
    return sum(expense['amount'] for expense in expenses)

def filter_expenses_by_category(expenses):
    category = choose_category()
    filtered_expenses = [expense for expense in expenses if expense['category'] == category]
    if filtered_expenses:
        print_expenses(filtered_expenses)
    else:
        print("No expenses found for this category.")

def save_expenses_to_file(expenses, filename="expenses.txt"):
    with open(filename, "w") as file:
        for expense in expenses:
            file.write(f"{expense['amount']}, {expense['category']}, {expense['date']}\n")

def load_expenses_from_file(filename="expenses.txt"):
    expenses = []
    try:
        with open(filename, "r") as file:
            for line in file:
                values = line.strip().split(", ")
                if len(values) == 2:
                    amount, category = values
                    date = "Unknown"  # Assign a default date if missing
                else:
                    amount, category, date = values
                expenses.append({'amount': float(amount), 'category': category, 'date': date})
    except FileNotFoundError:
        pass  # Ignore if the file doesn't exist yet
    return expenses

def remove_expense(expenses):
    print_expenses(expenses)
    try:
        index = int(input("Enter the number of the expense to remove: ")) - 1
        if 0 <= index < len(expenses):
            expenses.pop(index)
            save_expenses_to_file(expenses)
            print("Expense removed successfully.")
        else:
            print("Invalid index. No expense removed.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def choose_category():
    categories = ["Eating out & Takeaway", "Entertainment", "Fees", "Groceries", "Laundry", "Refund", "Subscriptions", "Shopping", "Transport", "Transfers", "Other"]
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category}")
    while True:
        try:
            choice = int(input("Choose a category by number: "))
            if 1 <= choice <= len(categories):
                return categories[choice - 1]
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    expenses = load_expenses_from_file()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Remove Expense")
        print("4. Filter Expenses by Category")
        print("5. View Total Expenses")
        print("6. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            amount = float(input("Enter amount: "))
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(expenses, amount, date)
        elif choice == "2":
            print_expenses(expenses)
        elif choice == "3":
            remove_expense(expenses)
        elif choice == "4":
            filter_expenses_by_category(expenses)
        elif choice == "5":
            print(f"Total Expenses: {total_expenses(expenses)}")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
