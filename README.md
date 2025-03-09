## Expense Tracker

## Description
This is a simple Expense Tracker program written in Python that allows users to track their expenses, categorize them, and filter them based on categories. The program saves expenses to a file and allows users to remove incorrect entries. 

Based from freeCodeCamp project (https://www.freecodecamp.org/learn/scientific-computing-with-python/#learn-lambda-functions-by-building-an-expense-tracker).

## Features
- Add expenses with amount, date, and category selection.
- View all recorded expenses.
- Remove an expense entry.
- Filter expenses by category.
- Calculate and display the total expenses.
- Data persistence through a text file (`expenses.txt`).

## Installation
### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone this repository or download the `expense-tracker.py` file.
2. Open a terminal or command prompt and navigate to the project folder.

## Usage
Run the program using the following command:
```bash
python3 expense-tracker.py
```

Follow the on-screen menu to:
1. Add an expense by entering the amount, selecting a category, and providing a date.
2. View recorded expenses.
3. Remove an incorrect entry.
4. Filter expenses by category.
5. View total expenses.
6. Exit the program.

## Categories
Users can select a category by entering its corresponding number:
1. Eating out & Takeaway
2. Entertainment
3. Fees
4. Groceries
5. Laundry
6. Refund
7. Subscriptions
8. Shopping
9. Transport
10. Transfers
11. Other

## Data Storage
Expenses are stored in `expenses.txt` in the following format:
```
amount, category, date
```
Example:
```
25.50, Groceries, 2024-03-09
15.00, Transport, 2024-03-08
```

## Contributing
Feel free to submit pull requests or report issues to improve this project!

## License
This project is open-source and free to use.

