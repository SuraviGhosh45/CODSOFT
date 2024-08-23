while True:
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Division & remainder\n6. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        print("After Adding Two Numbers:", num1 + num2)
    elif choice == 2:
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        print("After Subtracting Two Numbers:", num1 - num2)
    elif choice == 3:
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        print("After Multiplying Two Numbers:", num1 * num2)
    elif choice == 4:
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        if num2 != 0:
            print("After Dividing Two Numbers, The Division is:", num1 / num2)
        else:
            print("Division by zero is not allowed.")
    elif choice == 5:
        num1 = float(input("Enter 1st Number: "))
        num2 = float(input("Enter 2nd Number: "))
        if num2 != 0:
            print("After Dividing Two Numbers, The Division is:", num1 / num2)
            print("And The remainder is:", num1 % num2)
        else:
            print("Division by zero is not allowed.")
    elif choice == 6:
            print("Thanks For Visiting!")
            break
    else:
        print("Invalid choice.")
