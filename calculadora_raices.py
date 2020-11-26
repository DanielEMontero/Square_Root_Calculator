###########################################################
###########################################################

################ SQUARE ROOT CALCULATOR ###################

###########################################################

####################### DESCRIPTION #######################
# This program let you calculate a square root of a any
# positive number with three differents methods.
# The user can select the method of calculation.

######################### AUTHOR ##########################
# Ing. DANIEL EDUARDO MONTERO RAMÍREZ


import sys


def exhaustive(number,answer):
    while answer**2 < number:
        answer += 1
    if answer**2 == number:
        return answer
    else:
        answer = False
        return answer


def Approximate(number,answer):
    epsilon = 0.01
    step = epsilon**2

    while abs(answer**2 - number) >= epsilon and answer <= number:
        answer += step
    if abs(answer**2 - number) >= epsilon:
        answer = False
    
    return answer


def Binary(number):
    epsilon = 0.01
    lower = 0.0
    upper = max(1.0, number)
    answer = (upper + lower)/2

    while abs(answer**2 - number) >= epsilon:
        if answer**2 < number:
            lower = answer
        else:
            upper = answer
        
        answer = (lower + upper)/2

    return answer


def main():
    answer = 0
    number = input('Please insert a number to estimate his square root: ')
    method = input('Now Select a method: \n 1. Exhaustive Enumeration \n 2. Approximate Solution \n 3. Binary Substraction. \n Your method: ')
    try:
        number = float(number)
        method = int(method)
    except:
        print('Please insert a valid character. Only positive numbers and valid method')
        sys.exit()  
    if method <0 or method > 3 or number < 0:
        print('Please insert a valid character. Only positive numbers and valid method')
        sys.exit()
        
    if method == 1:
        value = exhaustive(number,answer)
    elif method == 2:
        value = Approximate(number,answer)
    else:
        value = Binary(number)
    
    if value == False:
        print(f'The number {number} has not a exactly square root')
    else:
        print(f'The square root of {number} is {value}.')


if __name__ == "__main__":
    main()