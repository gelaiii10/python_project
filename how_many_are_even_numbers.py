#input a counter for even numbers
even_count = 0
#ask user to input 10 numbers
for i in range(10):
    num = int(input(f"Enter Number {i + 1}: "))
    if num % 2 == 0: #compute if the number is even
        even_count += 1

print(even_count) #print the even numbers