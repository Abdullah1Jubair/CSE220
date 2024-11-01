def rotateLeft(source,k):
    n = len(source)
    temp = source[:k]
    for i in range(n-k):
        source[i]= source[i+k]
    for i in range(k):
        source[n - k + i] = temp[i]    
          
    print(source)
    
source=[10,20,30,40,50,60]    
rotateLeft(source,3)    
