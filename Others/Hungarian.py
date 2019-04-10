class solution():
    def hungarian(self, matrix):
        hung_matrix = matrix.copy()

        for i in range(len(hung_matrix)):
            min_row = min(hung_matrix[i])
            hung_matrix[i] = [x - min_row for x in hung_matrix[i]]

        for j in range(len(hung_matrix[0])):
            min_col = min(hung_matrix[i][j] for i in range(len(hung_matrix)))
            for j in range(len(hung_matrix)):
                hung_matrix[i][j] = hung_matrix[i][j] - min_col

