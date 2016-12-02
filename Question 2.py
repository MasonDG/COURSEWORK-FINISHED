def zeroes(x):
    factorial = x
    zeroes = 0
    #the following code is performed as many times as the value of the factorial number in increments of one
    for factorial in range(1,factorial+1):          
        
        #run the function as long as a number exists
        while factorial >  0:
            
            #if the number can no longer be divided whole by 5, break the function, otherwise add 1 to zeroes and divide factorial number by 5, then run whilst it still meets the while loop.

            if factorial % 5 != 0:
                #every time 5 can be divided to give no remainder, a zero is added. the number passed is ran through the conditionals again.
                  break
            else:
                  factorial = factorial / 5
                  zeroes = zeroes + 1
    return zeroes
