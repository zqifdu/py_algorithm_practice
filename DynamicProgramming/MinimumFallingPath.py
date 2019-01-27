
def minimumFallingPath(matrix):
    # What to return if no path???
    if not matrix:
        return None
    if not matrix[0]:
        return None
    if len(matrix[0]) == 1:
        return sum(x[0] for x in matrix)

    # TO OPTIMIZE: use only two rows (see minimumFallingPath2)
    dp = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]
    for row in range(1, len(matrix)):
        for col in range(len(matrix[0])):
            if col == 0:
                dp[row][col] = min(dp[row-1][col], dp[row-1][col+1])  + matrix[row][col]
            elif col == len(matrix[0]) - 1:
                dp[row][col] = min(dp[row-1][col-1], dp[row-1][col]) + matrix[row][col]
            else:
                dp[row][col] = min(dp[row-1][col-1], dp[row-1][col], dp[row-1][col+1]) + matrix[row][col]
    return min(dp[-1])

# Space optimization version
def minimumFallingPath2(matrix):
    if not matrix:
        return None
    if not matrix[0]:
        return None
    if len(matrix[0]) == 1:
        return sum(x[0] for x in matrix)

    # TO OPTIMIZE: use only two rows
    dp = [[matrix[i][j] for j in range(len(matrix[0]))] for i in range(2)]
    for row in range(1, len(matrix)):
        for col in range(len(matrix[0])):
            if col == 0:
                dp[row % 2][col] = min(dp[(row - 1) % 2][col], dp[(row - 1) % 2][col + 1]) + matrix[row][col]
            elif col == len(matrix[0]) - 1:
                dp[row % 2][col] = min(dp[(row - 1) % 2][col - 1], dp[(row - 1) % 2][col]) + matrix[row][col]
            else:
                dp[row % 2][col] = min(dp[(row - 1) % 2][col - 1], dp[(row - 1) % 2][col], dp[(row + 1) % 2][col + 1]) + matrix[row][col]
    return min(dp[row % 2])

# test cases:
matrix = []
assert minimumFallingPath(matrix) is None
assert minimumFallingPath2(matrix) is None

matrix = [[], []]
assert minimumFallingPath(matrix) is None
assert minimumFallingPath2(matrix) is None

matrix = [[1], [3]]
assert minimumFallingPath(matrix) == 4
assert minimumFallingPath2(matrix) == 4

matrix = [[1, 2], [3, 4]]
assert minimumFallingPath(matrix) == 4
assert minimumFallingPath2(matrix) == 4

matrix = [[1, 2], [4, 3]]
assert minimumFallingPath(matrix) == 4
assert minimumFallingPath2(matrix) == 4

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
assert minimumFallingPath(matrix) == 12
assert minimumFallingPath2(matrix) == 12

matrix = [[-10, 5, 2], [-1, -2, 3]]
assert minimumFallingPath(matrix) == -12
assert minimumFallingPath2(matrix) == -12


