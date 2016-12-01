#there is a bug where the last part of any passed list is ignored when the second to last lower value is detected
def maxSubSeq(x):
    #this list holds the current longest sub sequence in ascending order.
    tempList = [ ]
    #this variable controls where the function starts checking for ascending order from.
    position = 0
    #this variable gets updated with the value for the highest length for sub sequence everytime a new longest length is discovered.
    maxLenSubSec = 0
    #for every element in the list
    for i in range(1,len(x)):
        #if the current elements value is lower than the previous element, break off the list and add it into the tempList variable.
        #from the start position to the offending element
            if x[i]<x[i-1]:
                tempList.append(x[position:i])
                #when this if statement is true, update the position variable to start from the next element
                position = i
            
                
            
#iterate through each sub sequence within a list in the tempList list variable, same rule applies of if the longest sub sequence is detected except
                # it applies to the length of the list, when it finishes iterating, it will return the longest sub sequence
                
    for i in range(len(tempList)):
        if len(tempList[i]) > len(tempList[i-1]):
            maxLenSubSec = i
        
    return(tempList[maxLenSubSec])

    #return(tempList)




numbers = [1,2,3,4,1,5,1,6,7]
