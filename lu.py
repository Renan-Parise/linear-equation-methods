import numpy as np

def decomposicao_LU(matriz):
    n = len(matriz)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Fatorização LU
        L[i][i] = 1
        for j in range(i, n):
            U[i][j] = matriz[i][j]
            for k in range(i):
                U[i][j] -= L[i][k] * U[k][j]
        for j in range(i + 1, n):
            L[j][i] = matriz[j][i]
            for k in range(i):
                L[j][i] -= L[j][k] * U[k][i]
            L[j][i] /= U[i][i]

    return L, U

def resolver_sistema_LU(L, U, b):
    n = len(b)
    y = np.zeros(n)
    x = np.zeros(n)

    # Resolvendo Ly = b
    for i in range(n):
        y[i] = b[i]
        for j in range(i):
            y[i] -= L[i][j] * y[j]
        y[i] /= L[i][i]

    # Resolvendo Ux = y
    for i in range(n - 1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= U[i][j] * x[j]
        x[i] /= U[i][i]

    return x

# A = np.array([[1, 3, 5, 7], [3, 5, 7, 1], [5, 7, 1, 3], [7, 1, 3, 5]])
# b = np.array([12, 0, 4, 16])

A = np.array([[20, 7, 9], [7, 30, 8], [9, 8, 30]])
b = np.array([16, 38, 38])
L, U = decomposicao_LU(A)
x = resolver_sistema_LU(L, U, b)

print("Matriz L:")
print(np.round(L, decimals=1))
print("Matriz U:")
print(np.round(U, decimals=1))
print("Solução do sistema:")
print(np.round(x, decimals=1))