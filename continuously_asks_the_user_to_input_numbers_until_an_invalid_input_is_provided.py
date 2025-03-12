seen_numbers = set()  #to keep track unique numbers
print("input numbers (you need to type anything else to stop):")

while True:
    user_input = input("Enter a number: ")
    
    try: #try to convert input into float
        number = float(user_input)  # convert input to a number