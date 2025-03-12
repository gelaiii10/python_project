def main():
    #inout a list with a fixed size of 10
    numbers = [0] * 10
    #ask the user to input 10 numbers
    print("Please enter 10 numbers:")
    for i in range(10):
        while True:
            try:
                numbers[i] = int(input(f"Number {i + 1}: "))  # directly assign the number
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

  #display numbers, ensuring duplicates are only shown once
    print("duplicate numbers shown only once):")
    seen = set()
    for num in numbers:
        if num not in seen:
            print(num)
            seen.add(num)

if __name__ == "__main__":
    main()              