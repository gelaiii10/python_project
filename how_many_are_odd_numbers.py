#initialize the count of odd numbers to zero
odd_count = 0

# for loop to get 10 numbers from the user
for i in range(10):
#ask the user to input a number and convert it to int
    num = int(input(f"Enter Number {i + 1}: "))
#check if the number is odd
    if num % 2 != 0:
        odd_count += 1
#print the total count of odd numbers
print(odd_count)