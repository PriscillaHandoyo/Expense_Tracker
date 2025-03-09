from datetime import datetime

def add_expense(expenses, amount, category, date):
    expenses.append({'amount': amount, 'category': category, 'date': date})
    save_expenses_to_file(expenses)

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}, Date: {expense["date"]}')

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

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

def main():
    expenses = load_expenses_from_file()
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')

        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(expenses, amount, category, date)
        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
        elif choice == '3':
            print('\nTotal Expenses: ', total_expenses(expenses))
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses_by_category(expenses, category)
            print_expenses(expenses_from_category)
        elif choice == '5':
            print('Exiting the program.')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == "__main__":
    main()
