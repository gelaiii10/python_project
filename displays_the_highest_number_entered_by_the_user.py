highest_number = None #input highest number as none

while True:
    user_input = input("Enter a number: ")
        
        #check for exit condition
    if user_input.lower() == 'exit':
        break

    try:
        num = float(user_input)
            #update highest number if it's None or if the new number is greater
        if highest_number is None or num > highest_number:
                highest_number = num
    except ValueError:
            print("Invalid input. Please enter a valid number or type 'exit' to stop.")