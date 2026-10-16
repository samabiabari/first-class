num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

if op == "+":
    result = num1 + num2
    print("Answer: ", result)
elif op == "-":
    result = num1 - num2
    print("Answer: ", result)
elif op == "*":
    result = num1 * num2
    print("Answer: ", result)
elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print("Answer: ", result)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")