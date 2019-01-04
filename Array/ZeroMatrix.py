# Cracking the coding interview 1.8
def zero_matrix(matrix):
    if not matrix:
        return matrix
    if not matrix[0]:
        return matrix
    r_zero = set()
    c_zero = set()

    # scan through all the matrix elements and record the rows and cols that need to be set to zero
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                r_zero.add(r)
                c_zero.add(c)
    # set some rows to zero
    for r in r_zero:
        for col in range(len(matrix[0])):
            matrix[r][col] = 0
    # set some cols to zero
    for c in c_zero:
        for row in range(len(matrix)):
            matrix[row][c] = 0

    return matrix


# test cases
# Empty matrix
matrix = []
assert zero_matrix(matrix) == matrix

matrix = [[]]
assert zero_matrix(matrix) == matrix

matrix = [[], [], []]
assert zero_matrix(matrix) == matrix

# No zero
matrix = [[1], [1]]
assert zero_matrix(matrix) == matrix

# All elements are set to zero
matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
assert zero_matrix(matrix) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Non-square matrix and partial set
matrix = [[0, 1], [1, 1], [1, 1]]
assert zero_matrix(matrix) == [[0, 0], [0, 1], [0, 1]]

# zeros in the same row
matrix = [[0, 1, 0, 1], [1, 1 ,1, 1]]
assert zero_matrix(matrix) == [[0, 0, 0, 0], [0, 1, 0, 1]]