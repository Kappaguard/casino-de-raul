import random

def is_prime(number):
    for i in range(2,number//2):
        if (number % i) == 0:
            return "Число "+str(number)+ " не простое!"
    return "Число-то, " +str(number)+", простое!"

print(is_prime(23))

