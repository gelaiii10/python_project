
numbers = [0] * 10  #create a list with 10 elements initialized to 0

#ask the user to input 10 numbers
for i in range(10):
        numbers[i] = float(input(f"Enter number {i + 1}: "))

#first number
first_number = numbers[0]
#compute the result of the first number minus all remaining numbers
result = first_number
for num in numbers[1:]:
        result -= num