def validation(number,method):
    try:
        number = int(number)
        method = int(method)
    except:
        print('Please insert a valid character. Only numbers')
        quit


def main():
    number = input('Please insert a number to estimate his square root: ')
    method = input('Now Select a method: /n 1. Exhaustive Enumeration /n 2. Approximate Solution /n 3. Binary Substraction: ')
    validation(number, method)



if __name__ == "__main__":
    main()