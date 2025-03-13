numbers = [0] * 100  #initialize a list with a fixed size
count = 0  #to keep track of the number of valid inputs

while True:
    user_input = input("Enter a number: ")
        #check for exit condition
    if user_input.lower() == 'exit':
            break