def primeCheck(number, divider=2):
    #if the passed number is 2, then its already a prime number.
    if number == 2:  
        isPrimeNum = True
    #if the number is either 1 or 0, then it is not a prime number.
    elif number < 1 or number == 1:
        isPrimeNum = False
    #if the current number can divide N to give no remainders before then it is not a prime number.
    elif number % divider == 0: 
        isPrimeNum = False
    #if the dividing number is equal to N, it is a prime number
    elif divider * divider > number: 
        isPrimeNum = True
    #The recursion function recalls the function but adds 1 to the dividing number.
    else:
        isPrimeNum = primeCheck(number, divider+1)
    return isPrimeNum
