import numpy as np
def decrypt_matrix(matrix):
    row,col = matrix.shape
    col_sum = np.zeros(col,dtype = int)
    for i in range(col):
        for j in range(row):
            col_sum[i] += matrix[j,i]
    col_def = np.zeros(col-1,dtype= int) 
    for i in range(1,col):
        col_def[i - 1] = col_sum[i] - col_sum[i - 1]
        
    return col_def    
        
           
matrix =np.array([[1,3,1],
                 [6,4,2],
                 [5,1,7],
                 [9,3,3],
                 [8,5,4]
                 ])  
print(decrypt_matrix(matrix))
