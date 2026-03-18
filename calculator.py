print("Simple Calculator")

num1 = float(input("Enter first number: "))

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Square")

choice = input("Choose operation (1/2/3/4/5): ")

if choice == "1":
    num2 = float(input("Enter second number: "))
    print("Result:", num1 + num2)

elif choice == "2":
    num2 = float(input("Enter second number: "))
    print("Result:", num1 - num2)

elif choice == "3":
    num2 = float(input("Enter second number: "))
    print("Result:", num1 * num2)

elif choice == "4":
    num2 = float(input("Enter second number: "))
    print("Result:", num1 / num2)

elif choice == "5":
    print("Result:", num1 * num1)

else:
    print("Invalid choice")
