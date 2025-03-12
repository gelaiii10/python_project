#ask user to input two numbers and convert it to float
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
#check if the second number is not zero to avoid division by zero
if num2 == 0:
    print("ERROR: Division by zero is not allowed.")
else:
    #calculate the quotient of the two numbers
    quotient = num1/num2
    #print the product
    print("The quotient os the two numbers is:", quotient)

