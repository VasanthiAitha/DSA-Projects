#Attendence Tracker
student_name=""
student_status=""
def show_menu():
    print("\n-----Attendence tracker-----")
    print("1.Add attendence")
    print("2.View Attendence")
    print("3.Exit")
def add_attendence():
    global student_name
    global student_status

    student_name=input("Enter the Name of Student")
    student_status=input("Enter student(Present/Absent)")
    print("Attendence Added Sucessfully")
def view_attendence():
    if student_name == "":
        print("No attendence record found")
    else:
        print("----Attendence Record-----")
        print(student_name,"-",student_status)
def main():
    while True:
        show_menu()
        choice = input("Enter your choice")
        if choice=="1":
            add_attendence()
        elif choice =="2":
            view_attendence()
        elif choice=="3":
            print("Exiting the program")
            break
        else:
            print("Invalid Choice.Try Again")
main()