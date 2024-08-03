print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Division & remainder")
choice = int(input("Enter Choice: "))
num1 = float(input("Enter 1st Number: "))
num2 = float(input("Enter 2nd Number: "))
match choice:
    case 1:
        print("After Adding Two Numbers:", num1 + num2)
    case 2:
        print("After Subtracting Two Numbers:", num1 - num2)
    case 3:
        print("After Multiplying Two Numbers:", num1 * num2)
    case 4:
        if num2 != 0:
            print("After Dividing Two Numbers, The Division is:", num1 / num2)
        else:
            print("Division by zero is not allowed.")
    case 5:
        if num2 != 0:
            print("After Dividing Two Numbers, The Division is:", num1 / num2)
            print("And The remainder is:", num1 % num2)
        else:
            print("Division by zero is not allowed.")
    case _:
        print("Invalid choice. Please select a valid option.")
print("Thanks For Visiting!")
