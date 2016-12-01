def mAdd (a,b):
    #results of calculation are saved in a new list.
    result = [[0,0],[0,0]]
    #for every row in matrice A, the following code is conducted.
    for i in range(len(a)):
   #for every column in matrice A, the following code is conducted.
       for j in range(len(a[0])):
           #takes the relevant values in the nested list and assigns a value to result.
           result[i][j] = a[i][j] + b[i][j]
    return(result)

def mSub(a,b):
    result = [[0,0],[0,0]]
    #for every row in matrice A, the following code is conducted.
    for i in range(len(a)):
       #for every column in matrice A, the following code is conducted.
       for j in range(len(a[0])):
           #takes the relevant values for each nested list and subtracts them to give result a new  value.
           result[i][j] = a[i][j] - b[i][j]
    return(result)

def mMulti(a,b):
    result = [[0,0],[0,0]]
    #for every row in matrice A, the following code is conducted.
    for i in range(len(a)):
       #for every column in matrice B, the following code is conducted.
       for j in range(len(b[0])):
       #for every row in matrice B, the following code is conducted.
          for k in range(len(b)):
           #takes the following values at the time, multiplies the elements within and assigns the next available space the result.
           result[i][j] += a[i][k] * b[k][j]
    return(result)

def double(a):
    #this function doubles whatever matrice is passed through, this is used in the section of the equation that requires 2*(B+C) 
    return([[element*2 for element in matrice] for matrice in a])

b = [[12,7],[4,5]]
c = [[5,8],[6,7]]
a = mSub(mMulti(b,c),double(mAdd(b,c)))
