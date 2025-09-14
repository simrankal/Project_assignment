import csv
import os
from datetime import datetime

# Constants
FILENAME = 'expenses.csv'
FIELDS = ['Date', 'Category', 'Description', 'Amount']


def initialize_file():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(FIELDS)


def add_expense():
    """Add a new expense to the CSV file."""
    date = input("Enter date (YYYY-MM-DD) [Leave blank for today]: ") or datetime.now().strftime('%Y-%m-%d')
    category = input("Enter category (e.g., Food, Transport, Rent): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount! Expense not saved.")
        return

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
    
    print("✅ Expense added successfully!")


def view_expenses(filter_by=None, value=None):
    """View all expenses or filter by category/date."""
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        expenses = list(reader)

    if filter_by and value:
        expenses = [row for row in expenses if row[filter_by].lower() == value.lower()]

    if not expenses:
        print("No expenses found.")
        return

    total = 0
    print(f"\n{'Date':<12} {'Category':<15} {'Description':<25} {'Amount':>10}")
    print("-" * 65)
    for row in expenses:
        print(f"{row['Date']:<12} {row['Category']:<15} {row['Description']:<25} ${float(row['Amount']):>8.2f}")
        total += float(row['Amount'])

    print("-" * 65)
    print(f"{'Total':<54} ${total:>8.2f}\n")


def menu():
    """Main menu for the expense tracker."""
    while True:
        print("\n===== Personal Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View by Category")
        print("4. View by Date")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            category = input("Enter category to filter by: ")
            view_expenses(filter_by='Category', value=category)
        elif choice == '4':
            date = input("Enter date to filter by (YYYY-MM-DD): ")
            view_expenses(filter_by='Date', value=date)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    initialize_file()
    menu()
