numbers = []
    
while True:
    user_input = input("input a number: ")
           
    if user_input.lower() == 'exit': #check for exit condition
        break

    try:
        num = float(user_input) #try to convert input into float
        numbers.append(num)  #add the number to the list
    except ValueError:
        print("Invalid input. Please enter a valid number or type 'exit' to stop.")

if not numbers: #inform the user if no number were entered
        print("No numbers were entered.")
          
#find the number with the most duplicates
most_duplicates = max(set(numbers), key=numbers.count)
max_count = numbers.count(most_duplicates) 

print(most_duplicates) #print the most duplicate numbers