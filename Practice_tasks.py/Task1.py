import numpy as np
def union_of_arrays(a, b):
    result = np.zeros(10,dtype=int)
    for i in range(len(a)):
        result[i] = a[i]
    for i in range(len(a)):
        if b not in a:
            result[len(a)+i]      =  b[i]
    
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])

result,count = union_of_arrays(a, b)
print("Union of the two arrays:", result)
print("count is",count)
print(type(result))
