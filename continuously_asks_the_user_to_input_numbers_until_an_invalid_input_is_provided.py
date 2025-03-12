seen_numbers = set()  #to keep track unique numbers
print("input numbers (you need to type anything else to stop):")

while True:
    user_input = input("Enter a number: ")
    
    try: #try to convert input inti float
        number = float(user_input)  #convert input to a number
        #check if the number is already in the set
        if number in seen_numbers:
            print("duplicate")
        else:
            print("unique")
            seen_numbers.add(number)  #add the number to the set

    except ValueError:
        print("Invalid input. Exiting the program.")
        break  #exit the loop if input is invalid      