numbers = [0] * 100  #initialize a list with a fixed size
count = 0  #to keep track of the number of valid inputs

while True:
    user_input = input("Enter a number: ")
        #check for exit condition
    if user_input.lower() == 'exit':
            break
    
    try:
        num = float(user_input) #convert input into float
        numbers[count] = num  #directly assign the number to the list
        count += 1  #increment the count of valid numbers
    except ValueError:
        print("Invalid input. Please enter a valid number or type 'exit' to stop.")

if count > 0:
    average = sum(numbers[:count]) / count  #compute average using only valid entries
    print(average)
else:
    print("No valid numbers were entered.")        