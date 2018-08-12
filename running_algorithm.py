# main algorithm along with time taken to test primality
import main_file_with_time_diff as base
try:
    print('Enter any integer to check whether it is prime or not : ')
    number_to_check = int(input())
    #calling the function to check primality from main module
    result = (base.check_prime(number_to_check))
    print(result,'ms')
except:
    '''
    Handling of non-numeric data including floating point numbers    
    '''
    print("Please don't try to fool the algorithm")