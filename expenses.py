import json
filename = 'data.txt'
def initialize_file():
    with open(filename, 'r') as file:
        file.read()    
        with open(filename, 'w') as file:
            file.write("Date,Category,Amount\n")
def add_expenses(date, category, amount):
    with open(filename, 'a') as file:
        file.write(f"{date}, {category}, {amount}\n")
    
def view_expenses(search):
    with open(filename,'r') as file:
        view = json.loads(filename)
        print(view[search])
        

def total_expenses():
    pass

while True:
    print("WELCOME TO EXPENSES TRACKER ")
    print(
                """List of operations you can perform
                                    1.Add Expenses with details
                                    2.View expenses by category
                                    3.Display the total expenses""")
    choice = input("enter your choice via 1/2/3: ")
    if choice == '1':
        date = input("enter the date(dd/mm/yy): ")
        amount = float(input("enter the amount you spend: "))
        category = input("enter the category you spend the money: ")
        add_expenses(date, category, amount)
    elif choice == '2':
        search_category = input("enter the category from which you want to see the expenses: ")
        view_expenses(search_category)
    elif choice == '3':
        pass
    choice2 = input("""Do You Want To Perform More Operations
                    'y' for YES 'n' for NO: """)
    if choice2 == 'n':
        print("THANK YOU FOR USING EXPENSE TRACKER.")
        break
