print("numbers from 0 to 100 except ending in 0 or 5:")
#use for loop to iterate from 0 to 100
for i in range(101): #range(101) goes from 0 to 100 inclusive
    if i % 10 != 0 and i % 10 != 5: #check if the number ends in 0 or 5
        print(i)