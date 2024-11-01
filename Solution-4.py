num1= float(input("enter the first number: "))
operator = input("enter an operator (+,-,*,/,%): ")
num2 = float(input("enter the second number: "))

if operator == '+':
    result = num1 + num2
    print(f"The result is: {result}")
elif operator == '-':
    result = num1 - num2
    print(f"The result is: {result}")
elif operator == '*':
    result = num1 * num2 
    print(f"The result is: {result}")
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print(f"Error: Division by 0 is not allowd") 
elif operator == '%':
    if num2 != 0:
        result = num1 % num2
        print(f"The remainder result is: {result}")
    else:
        print(f"Error: Division by zero is not allowed")    
else:
    print("Invalid operator: Please enter one of +, -, *, /, or %.")        



       





