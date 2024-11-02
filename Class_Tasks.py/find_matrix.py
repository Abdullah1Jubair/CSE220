import numpy as np

mat = np.array([[1, 2, 3], [4, 5, 6]])
mat2 = np.zeros((2, 2), dtype=int)

def find_value(matrix, value):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == value:
                print(f"Value {value} found at position ({i}, {j})")
                return True  
    print(f"Value {value} not found in the matrix.")
    return False  
num = 5
find_value(mat, num)
