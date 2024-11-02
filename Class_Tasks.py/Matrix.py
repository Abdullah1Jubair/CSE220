import numpy as np
mat = np.array([[1,2,3],[4,5,6,]])
mat2 = np.zeros ((2,2),dtype = int)
def print_matrix(mat):
    row,col = mat.shape #(2,3)
    for i in range(row):
        for j in range(col):
            print(mat[i][j], end= " ")
            
        print()
print_matrix(mat)        