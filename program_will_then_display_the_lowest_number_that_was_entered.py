#add a variable to store the lowest number
lowest_number = None
print("Enter numbers (you need to type anything else to stop):")

while True:
    user_input = input("Enter a number: ")
#try to convert the input to a float
    try:
        number = float(user_input)  #convert input to a number
#update the lowest number if it is the first valid input or if it is lower than the current lowest
        if lowest_number is None or number < lowest_number:
            lowest_number = number

    except ValueError:
        #exit the loop if input is invalid
        print("Invalid input. Exiting the program.")
        break