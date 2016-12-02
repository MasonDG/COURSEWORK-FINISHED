def reverseOrder(sentence):
    #Two variables, word is the elements catched before spaces, sentenceReversed stores them in reverse order"
    word = ""
    sentenceReversed = ""
    #for every element in the passed string.
    for i in sentence:
        #if the element is a space;
        if i == ' ' or  i == "," or i == ".":
            #this variable takes on any values passed into the word variable and resets its value.
            sentenceReversed = word + ' ' + sentenceReversed
            word = ''
        else:
            #the element is added to the word variable.
            word += i
    #the word variable is added onto whatever is already present within sentenceReversed in a past state.
    sentenceReversed = word + ' ' + sentenceReversed
    return sentenceReversed
#o n
