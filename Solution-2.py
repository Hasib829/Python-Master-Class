
average_mark = float(input("Enter the average mark: "))


if average_mark >= 90:
    print("The grade is: A+")
elif 70 <= average_mark < 90:
    print("The grade is: A-")
elif 50 <= average_mark < 70:
    print("The grade is: B")
else:
    print("The grade is: Fail")  
