import numpy as np

def print_matrix(matrix):
    """Prints the matrix in a readable format."""
    for row in matrix:
        print(" ".join(row))

def walk_zigzag(floor):
    """Walks through the matrix in a zigzag diagonal pattern and prints the elements."""
    rows, cols = floor.shape
    
    # Loop through each diagonal starting from each column of the first row
    for start_col in range(cols):
        row, col = 0, start_col
        diagonal_elements = []

        while row < rows and col >= 0:
            diagonal_elements.append(floor[row, col])
            row += 1
            col -= 1
        
        # Print the diagonal elements
        if diagonal_elements:  # Check if there are elements to print
            print(" ".join(diagonal_elements))

    # Loop through each diagonal starting from each row of the last column
    for start_row in range(1, rows):
        row, col = start_row, cols - 1
        diagonal_elements = []

        while row < rows and col >= 0:
            diagonal_elements.append(floor[row, col])
            row += 1
            col -= 1
        
        # Print the diagonal elements
        if diagonal_elements:  # Check if there are elements to print
            print(" ".join(diagonal_elements))

# Define the floor array
floor = np.array([[ '3' , '8' , '4' , '6' , '1'],
                  ['7' , '2' , '1' , '9' , '3'],
                  ['9' , '0' , '7' , '5' , '8'],
                  ['2' , '1' , '3' , '4' , '0'],
                  ['1' , '4' , '2' , '8' , '6']]
                )

print("Matrix:")
print_matrix(floor)  # Print the floor matrix
print('Walking Sequence:')
walk_zigzag(floor)   # Execute the zigzag walk
