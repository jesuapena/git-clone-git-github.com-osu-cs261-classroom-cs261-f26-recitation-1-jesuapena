import random
import time


def main():

    # Starting size of the n list
    n = 1000000

    #the list incrementation
    increment = 1000000
    print("n,time") #prints the header for the output, indicating that the first column is the size of the list (n) and the second column is the time taken to sort it.
    # Run the test 10 times
    for i in range(20): #runs the test 
        # Create an empty list
        numbers = []
        # Add n random numbers to the list
        for j in range(n):
            numbers.append(random.random()) #append wont affect the sorting time
        # Start timing
        start_time = time.perf_counter()
        numbers.sort()
        end_time = time.perf_counter() #Stop timing
        # Find how long sorting took
        sort_time = end_time - start_time #Find how long sorting took
        print(n,",", sort_time)#Print n and the sorting time
        # Increase the size of the next list
        n = n + increment
main()



#perf_counter() will help measure the time taken for sorting accurately