def add_expenses():
    pass

def view_expenses():
    pass

def total_expenses():
    pass

while True:
    print("WELCOME TO EXPENSES TRACKER ")
    print(
                """List of operations you can perform
                                    1.Add Expenses with details
                                    2.View expenses by category
                                    3.Display the total expenses""")
    while True:
            try:
                choice = int(input("enter your choice via 1/2/3: "))
                break
            except ValueError:
                print("PLEASE GIVE THE VALUE IN INTEGER FORM ONLY AND UPTO 3. ")
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    choice2 = input("""Do You Want To Perform More Operations
                    'y' for YES 'n' for NO: """)
    if choice2 == 'n':
        print("THANK YOU FOR USING EXPENSE TRACKER.")
        break
