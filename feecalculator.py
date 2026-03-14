# Fee Calculator
def calculate_fee(course,marks):
    if course == "AI":
        fee=50000
    elif course == "Web":
        fee=30000
    elif course == "Data Science":
        fee=40000
    else:
        return None # Invalid course
    
    #Discount Condition
    if marks >= 90:
        fee -=5000
    return fee
def main():
    course = input("Enter course (AI, Web, Data Science): ")
    marks = int(input("Enter marks: "))
    fee = calculate_fee(course, marks)
    if fee is not None:
        print(f"Final fee for {course} is: {fee}")
    else:
        print("Final fee:,fee")
main()