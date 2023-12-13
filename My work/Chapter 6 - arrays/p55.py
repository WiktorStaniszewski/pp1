def transpose_matrix(matrix):
    # Use the zip function to transpose the matrix
    transposed = [list(row) for row in zip(*matrix)]
    return transposed

# Test cases
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]
matrix_c = [[5, 6, 7, 8]]

# Display transposed matrices
print("Matrix A:")
for row in transpose_matrix(matrix_a):
    print(row)

print("\nMatrix B:")
for row in transpose_matrix(matrix_b):
    print(row)

print("\nMatrix C:")
for row in transpose_matrix(matrix_c):
    print(row)
