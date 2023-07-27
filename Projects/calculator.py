#Calculator using conditional statements

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter the operator: ")
if operator == '+':
    print("The addition of", a, b, "is: ", a+b)
elif operator == '-':
    print("The subration of", a, b, "is: ", a-b)
elif operator == '/':
    print("The division of", a, b, "is: ", a/b)
elif operator == '*':
    print("The multiplication of", a, b, "is: ", a*b)
else:
    print("Invalid operator")
