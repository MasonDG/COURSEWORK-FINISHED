def removeVowels(sentence):
    #nothing was entered
    if len(sentence)== 0 :
        #Nothing will be returned, this base case will be hit after the function so it has to return nothing.
        return(sentence)
    #check if the first value taken in the string is a vowel lowercase or uppercase.
    elif sentence[0] in "aeiou" or sentence[0] in "AEIOU":
        return removeVowels(sentence[1:])
    #returns the value and any other values that are excluded from the called functions recursion until there is nothing left in the initial string.
    return sentence[0] + removeVowels(sentence[1:])
