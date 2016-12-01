def rangeSearch(low, high, array):
    #bottom variable refers to the first position of the array
    bottom = 0
    #top variable is the last position of the array.
    top = len(array)-1
        #variable is set to false as nothing has been found yet
    rangeFind = False

    #this condition is true whilst bottom is not equal to the top position
    #and an element in the range specific has not been found
    while bottom <= top and rangeFind == False:
        #this is the pointer for the middle of the array 
        middle = (bottom+top)//2
        #if the mid point lands on an element(s) in which the value
        #is higher than the low variable but smaller than the high variable
        if array[middle]< high and array[middle] > low:
            found = True
            return str(found) + " " + str(array[middle])
            #if the pointer is only small than the high variable then the bottom
            #position is moved up.
        elif array[middle] < high:
            bottom = middle + 1
        elif array[middle] > low:
            #similar scenario for the first elif except it will move
            #the last element pointer back
            top = middle - 1
    #return whether a value was found
    return("No value exists between the specified ranges.")





mylist = [1,2,3,5,7,8,9,10,14,15]
