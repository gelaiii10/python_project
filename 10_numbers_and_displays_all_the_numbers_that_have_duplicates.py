#input a list with fixed size of 10
numbers = [0] * 10

#ask user to input 10 numbers
for i in range(10):
        while True:
            try:
                num = float(input(f"Number {i + 1}: "))
                numbers[i] = num  #assign the number to the list
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")