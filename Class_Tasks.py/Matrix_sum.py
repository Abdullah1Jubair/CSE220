import numpy as np
mat = np.array([[1,2,3],[4,5,6]])
mat2 = np.zeros((2,2),dtype=int)
def matrix_sum(mat):
    total_sum = 0 
    rows,cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            total_sum += mat[i][j]
            print(mat[i][j], end =" ")
        print()    
    return total_sum            
result = matrix_sum(mat)
print("ur sum is",result)
