numbers = [] #add list to store the numbers

while True:
    user_input = input("Enter a number: ")

    #try to convert the input to a float
    try:
        number = float(user_input)  
        numbers.append(number)  #add the number to the list

    except ValueError:
        #exit the loop if input is invalid
        print("Invalid input. Exiting the program.")
        break