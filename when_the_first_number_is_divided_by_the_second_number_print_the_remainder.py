#ask user to input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num2 == 0: #check if the second number is not zero to avoid division by zero
    print("ERROR: Division by zero is not allowed.")
else:
    remainder = num1 % num2 #compute the remainder
    print(remainder) #print the remainder