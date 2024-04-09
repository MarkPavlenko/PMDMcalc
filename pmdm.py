operation = input("hint: + - / *. type the symbol here:")

if operation == "+":
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    result = num1 + num2
    print(result)

if operation == " +":
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    result = num1 + num2
    print(result)

elif operation == "-":
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    result = num1 - num2
    print(result)

elif operation == " -":
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    result = num1 - num2
    print(result)

elif operation == "/":
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    result = num1 / num2
    print(result)

elif operation == " /":
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    result = num1 / num2
    print(result)

elif operation == "*":
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    result = num1 * num2
    print(result)

elif operation == " *":
    num1 = float(input("Number 1:"))
    num2 = float(input("Number 2:"))
    result = num1 * num2
    print(result)

else:
    print("Your symbol is not supported in PMDMcalc. Please try again with another symbol.")


