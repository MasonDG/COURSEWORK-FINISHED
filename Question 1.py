#The Rationale behind this implemented algorithm is that it takes an
#existing list and based on the length of the list and a random integer,
#if the value pulled matches the current state of the list, it will
#write out that specific entry into a new list then repeat until all previous entries are written into the new list.
import random

def array(x):
    #makes a integer of the list's length 
    length = len(x) - 1
    #for loop for every entry from the passed list
    for i in range(length, 0, -1):
        #value variable can be anything from 0 to the length of the list being passed..
        value = random.randint(0,i)
        #If the value matches the integer being passed it will ignore it as its already sorted
        if value == i:
            pass
        #Rearranges the value selected to the first available position.
        x[value],x[i] = x[i], x[value]
    #prints the shuffled list
    return x


#The list to be used
myArray = [5,3,8,6,1,9,2,7]


#Does my algorithm have defined Inputs and Outputs?
 #Yes, the Inputs are myArray and outputs are the returned x

#It does terminate

#The code is specified clearly and shows exactly what happens each line.

# The algorithm will reshuffle the list passed to the function every time with differing shuffles.
