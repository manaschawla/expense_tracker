import json
import matplotlib.pyplot as plt

# File to store the expenses
file_name = "expenses2.json"

# Load existing expenses from the file
def load_expenses():
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save expenses to the file
def save_expenses(expenses):
    with open(file_name, 'w') as file:
        json.dump(expenses, file, indent=4)

# Add a new expense
def add_expense(date, amount, category, description):
    expenses = load_expenses()
    expenses.append({
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    })
    save_expenses(expenses)

# View all expenses
def view_all_expenses():
    expenses = load_expenses()
    for expense in expenses:
        print(f"Date: {expense['date']}, Amount: {expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")

# View expenses by category
def view_expenses_by_category(category):
    expenses = load_expenses()
    for expense in expenses:
        if expense['category'] == category:
            print(f"Date: {expense['date']}, Amount: {expense['amount']}, Description: {expense['description']}")

# Calculate the total amount spent
def total_amount():
    expenses = load_expenses()
    total = 0
    for expense in expenses:
        total += expense['amount']
    print(f"Total Amount Spent: {total}")
# Show bar graph for daily expenses
def bar_graph_daily():
    expenses = load_expenses()
    daily_expenses = {}
    for expense in expenses:
        if expense['date'] in daily_expenses:
            daily_expenses[expense['date']] += expense['amount']
        else:
            daily_expenses[expense['date']] = expense['amount']
    
    dates = list(daily_expenses.keys())
    amounts = list(daily_expenses.values())

    plt.bar(dates, amounts, color='blue')
    plt.xlabel('Date')
    plt.ylabel('Amount Spent')
    plt.title('Daily Expenses')
    plt.show()

# Show pie chart for category expenses
def pie_chart_category():
    expenses = load_expenses()
    category_expenses = {}
    for expense in expenses:
        if expense['category'] in category_expenses:
            category_expenses[expense['category']] += expense['amount']
        else:
            category_expenses[expense['category']] = expense['amount']

    categories = list(category_expenses.keys())
    amounts = list(category_expenses.values())

    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title('Expenses by Category')
    plt.show()

while True:
    print("""EXPENSE TRACKER
          1.Add Expense.
          2.View All Expenses.
          3.View Expenses By Category.
          4.Total Amount Spend.
          5.Show bar graph for daily expenses.
          6.Show pie chart for category expenses.
          7.Exit""")

    choice = input("Choose an option: ")

    if choice == "1":
        date = input("Enter the date (YYYY-MM-DD): ")
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        description = input("Enter the description: ")
        add_expense(date, amount, category, description)
        print("Expense added successfully.")
    elif choice == "2":
        view_all_expenses()
    elif choice == "3":
        category = input("Enter the category: ")
        view_expenses_by_category(category)
    elif choice == "4":
        total_amount()
    elif choice == "5":
        bar_graph_daily()
    elif choice == "6":
        pie_chart_category()
    elif choice == "7":
        print("THANK YOU")
        break
    else:
        print("Invalid choice. Please try again.")