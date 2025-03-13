numbers = []  #input an empty list to store the numbers
    
while True:
    user_input = input("Enter a number: ")
        
    if user_input.lower() == 'exit': #check for exit condition
            break
    
    try:
        num = float(user_input)
        numbers.append(num)  #add the number to the list
    except ValueError:
        print("Invalid input. Please enter a valid number or type 'exit' to stop.")

    numbers.sort(reverse=True) #sort the numbers in descending order
    #display the sorted numbers
    if numbers:
        print("Numbers from highest to lowest:")
        for number in numbers:
            print(number)
    else:
        print("No valid numbers were entered.")