#import math class to use the floor and sqrt functions
import math
def perfectSquare(x):
    #When X is passed, the SQRoot is calculated and floored to give an integer to compare with the integer squared
    sqrtX = math.floor(x**(1/2))
    numSquared = sqrtX * sqrtX
                
#Return previous variable if the number passed is a perfect square, else return the closest perfect square after square rooting x  
    if int(x) == numSquared:
       return(str(sqrtX) + " is a perfect square of " + str(x))
    else:
        return("Not a perfect square, nearest is: " + str(round(x**(1/2))**2))
