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

numbers.sort() #sort the numbers in ascending order

if numbers: #display the sorted numbers
    print("Numbers from lowest to highest:")
    for num in numbers:
        print(num)
else:
    print("No valid numbers were entered.")
