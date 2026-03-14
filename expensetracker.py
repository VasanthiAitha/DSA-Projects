#Expense Tracker
expenses = []
def add_expense():
    name = input("Enter expense name: ")
    amount = input("Enter expense amount: ")
    expense={
        "name": name,
        "amount": amount
    }
    expenses.append(expense)
    print("Expense added ")
def view_expenses():
    for expense in expenses:
        print(expense["name"], expense["amount"])
def show_menu():
    print("\nExpense Tracker ")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")
main()