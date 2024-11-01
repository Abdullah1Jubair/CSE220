def leftshift(array,k):
    n = len(array)
    for i in range(n-k):
        array[i]= array[i+k]
    for i in range(n-k,n)    :
        array[i]= 0
    print(array)    

array=[10,20,30,40,50,60]       
leftshift(array,2) 