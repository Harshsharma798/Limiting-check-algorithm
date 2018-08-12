#actual cash behind the algorithm i.e. the major analyzer
import list_creator as lc
import datetime
from math import sqrt,floor

def check_prime(number):
    # starts the clock
    start_time = datetime.datetime.now()
    if number > 1:
        prime = True
        # list of all prime numbers before the square root of the number is grabbed from list_creater
        for i in lc.create_list(floor(sqrt(number))):
            # checks for the actual number with the numbers in prime number list
            if number % i == 0:
                prime = False
                break
        #excepts 2 and analyze the value of flag
        if prime or number == 2:
            print("Yes ", number, " is a prime number")
        else:
            print("No ", number, " is not a prime number")
    else:
        print("No ", number, " is not a prime number")

    #ending the clock
    end_time = datetime.datetime.now()
    time_diff = end_time - start_time
    total_time_in_ms = (time_diff.total_seconds()*1000)
    # total time taken
    return total_time_in_ms
    # print(datetime.timedelta(time_diff))
