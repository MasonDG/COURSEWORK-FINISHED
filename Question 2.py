def zeroes(x):
    factorial = x
    zeroes = 0
    #the following code is performed as many times as the value of the factorial number in increments of one
    for factorial in range(1,factorial+1):          
        
        #checks if the value entered is above or equal to 0
        while factorial >  0:
            #Check the number to see if it is divisible by 5
            if factorial % 5 != 0:
                #every time 5 can be divided to give no remainder, a zero is added. the number passed is ran through the conditionals again.
                break
            else:
                #Used to break out of the if statement or the function would never print
               factorial = factorial / 5
               zeroes = zeroes + 1
    return zeroes
