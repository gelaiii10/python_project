def main():
    #inout a list with a fixed size of 10
    numbers = [0] * 10
    #ask the user to input 10 numbers
    print("Please enter 10 numbers:")
    for i in range(10):
        while True:
            try:
                numbers[i] = float(input(f"Number {i + 1}: "))  # directly assign the number
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")