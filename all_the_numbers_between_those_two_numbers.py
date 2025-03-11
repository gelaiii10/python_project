#ask user to input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
#determine the upper and lower bounds
lower = min(num1, num2)
upper = max(num1, num2)

print(f"numbers between {lower} and {upper}:") #print all numbers between the two numbers
for i in range(lower + 1, upper): 
    print(i)