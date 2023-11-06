def gauss_elimination_with_pivoting(matrix, vector):
    n = len(vector)
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        vector[i], vector[max_row] = vector[max_row], vector[i]

        for j in range(i + 1, n):
            factor = matrix[j][i] / matrix[i][i]
            vector[j] -= factor * vector[i]
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = vector[i] / matrix[i][i]
        for j in range(i + 1, n):
            x[i] -= (matrix[i][j] * x[j]) / matrix[i][i]

        x[i] = round(x[i], 1)

    return x

matrix1 = [[2, 1, 1, 1], [1, 2, 1, 1], [1, 1, 2, 1], [1, 1, 1, 2]]
vector1 = [1, 2, 3, 4]
result1 = gauss_elimination_with_pivoting(matrix1, vector1)
print(result1)