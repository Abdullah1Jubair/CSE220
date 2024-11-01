def shiftRight(source,k):
    n = len(source)
  
    for i in range(n-1,k-1,-1):
        source[i]= source[i-k]
    for i in range(k):    
        source[i]= 0
        
    print(source)    


source=[10,20,30,40,50,60]
shiftRight(source,3)
