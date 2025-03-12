#range(101) goes from 0 to 100 inclusive
for i in range(0,101):
    if i % 2 == 0 and i % 10 != 0: #condition if the number does not ending in zero
        print(i) #print the result