#ask user to input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num2 == 0: #test if the 2nd number is  not 0 to avoid error
    print("ERROR: Division by zero is not allowed.")
else:
    quotient = int(num1//num2) #compute the quotient using integer division
    print(quotient)     #primt the quotient