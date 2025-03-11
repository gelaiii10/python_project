
numbers = [0] * 10  #create a list with 10 elements initialized to 0

#ask the user to input 10 numbers
for i in range(10):
        numbers[i] = int(input(f"Enter number {i + 1}: "))

#first number
first_number = numbers[0]

result = first_number #compute the result of the first number minus all remaining numbers
for num in numbers[1:]:
        result -= num

print(result) #print the result