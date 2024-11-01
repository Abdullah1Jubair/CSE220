#leftshifarray 
import numpy as np 
array = np.array([1,2,3,4,5])
def leftshift(array):
    n = len(array)
    for i in range(0,n-1,1):
        array[i]= array[i+1]
    array[n-1]= 0
    print("new array",array)    

print("previous array",array)        
leftshift(array)