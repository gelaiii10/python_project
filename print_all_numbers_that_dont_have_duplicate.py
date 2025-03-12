def main():
#input a list with a fixed size of 10
    numbers = [0] * 10

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
    unique_numbers = [num for num in numbers if numbers.count(num) == 1]              
#print numbers that do not have duplicate("Numbers without duplicates:")
    if unique_numbers:
        print(unique_numbers)
    else:
        print("all numbers have duplicates.")


if __name__ == "__main__":
    main()
