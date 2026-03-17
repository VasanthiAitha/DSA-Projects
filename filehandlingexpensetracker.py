expenses=[]
def export_expenses_to_file(expenses):
    with open("expenses.txt", "w") as file:
        for expense in expenses:
            file.write(expense['name'] +"," + expense['amount'] + "\n")
def main():
    while True:
        print("\nExpense Tracker ")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Export to File")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            name = input("Enter expense name: ")
            amount = input("Enter expense amount: ")
            expenses.append({"name": name, "amount": amount})
            print("Expense added ")
        elif choice == "2":
            for expense in expenses:
                print(expense["name"], expense["amount"]) 
        elif choice == "3":
            export_expenses_to_file(expenses) 
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Try again.")
main()
