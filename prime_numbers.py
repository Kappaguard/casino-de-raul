import math

def is_prime(number):
    for i in range(2,int(math.sqrt(number))+1):
        if ((number % i) == 0) and (i !=1 ):
            return False
    return True

print(is_prime(11149))

