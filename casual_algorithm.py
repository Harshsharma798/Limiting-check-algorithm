import datetime
try:
    print('Enter any integer to check whether it is prime or not : ')
    number = int(input())
    start_time = datetime.datetime.now()
    # flag for prime
    prime = True
    for i in range(2,int(number/2)):
        if (number % i) == 0:
            prime = False
            break

    # analyzing flag
    if prime:
        print("Yes it is a prime number")
    else:
        print("No it is not a prime number")

except:
    '''
    Handling of non-numeric data including floating point numbers    
    '''
    print("Please don't try to fool the algorithm")

end_time = datetime.datetime.now()

time_diff = end_time - start_time

#printing the time taken for algorithm to analyze
print(time_diff.seconds, 's ',time_diff.microseconds/1000, 'ms')