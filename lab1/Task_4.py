def rotateRight(source,k):
    n = len(source)
    temp = source[-k:]
    
    for i in range(n-k-1,-1,-1):
        source[i+k]= source[i]
        
    for i in range(k):
         source[i]= temp[i]
    print(source)         
source=[10,20,30,40,50,60]
rotateRight(source,3)
    