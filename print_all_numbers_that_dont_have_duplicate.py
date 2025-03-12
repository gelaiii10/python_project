#input a list with a fixed size of 10
numbers = 0 * 10

#use for loop to ask the user to input 10 numbers
print("you need to input 10 numbers:")
for i in range(10):
    while True:
        try:
            numbers[i] = int(input(f"Number {i + 1}: "))  #directly assign the number to the list
            break
        except ValueError:
                print("Invalid input. Please input a valid number.")
#find and display numbers without duplicates