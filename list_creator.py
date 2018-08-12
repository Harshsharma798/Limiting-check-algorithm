from math import floor,sqrt
def create_list(breakpoint):
    # flag for primality
    prime = True
    # 2 is a prime number so its already added
    prime_list = [2]
    for i in range(3,(breakpoint+1),2):
        for j in range(3,(floor(sqrt(i))+1)):
            # checks for every number before the squareroot
            if i % j == 0:
                prime = False
                break
        #analyzing the flag
        if prime:
            prime_list.append(i)
        prime = True

    # list of all prime numbers number passed as parameter
    return prime_list