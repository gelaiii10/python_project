#initialize the sum to zero
total_sum = 0

#use for loop to get 10 numbers from the user
for i in range(10):
    #Ask the user to input a number
    num = int(input(f"Enter number {i + 1}: "))
    total_sum += num #add number to the total sum

    #print the total sum
    print(total_sum)