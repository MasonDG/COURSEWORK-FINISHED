#The Rationale behind this implemented algorithm is that it takes an
#existing list and based on the length of the list and a random integer,
#if the value pulled matches the current state of the list, it will
#write out that specific entry into a new list then repeat until all previous entries are written into the new list.

import random

def shuffle(x):
      for i in range(0,len(x)):
            value = random.randint(0,i)
            x[value],x[i] = x[i],x[value]
      return(x)


array = [1,2,3,4,5,6]

#Does my algorithm have defined Inputs and Outputs?
 #Yes, the Inputs are myArray and outputs are the returned x

#It does terminate

#The code is specified clearly and shows exactly what happens each line.

# The algorithm will reshuffle the list passed to the function every time with differing shuffles.
