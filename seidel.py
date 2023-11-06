import numpy as np

def gauss_seidel(A, b, max_iterations=100, tol=1e-5):
    n = len(b)
    x = np.zeros(n)
    
    for iteration in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            x_new[i] = (b[i] - np.dot(A[i, :i], x_new[:i]) - np.dot(A[i, i+1:], x[i+1:])) / A[i, i]
        if np.all(np.abs(x_new - x) < tol):
            break
        x = x_new
    
    return x

# Teste 1
A1 = np.array([[10, 1, -2, 1, -3], [1, -8, 2, -3, 1], [2, -1, 7, -2, 1], [2, -3, 1, -1, 9], [1, -2, 1, -6, 1]], dtype=float)
b1 = np.array([-13, -14, -18, 18, 7], dtype=float)
x1 = gauss_seidel(A1, b1)
x1 = np.round(x1, 1)
print("Resultado do Teste 1:", x1)

# Teste 2
A2 = np.array([[4, 1, 1, -1], [3, 6, 1, 1], [1, 1, 8, 4], [2, 1, 1, 5]], dtype=float)
b2 = np.array([1, 3, 8, -9], dtype=float)
x2 = gauss_seidel(A2, b2)
x2 = np.round(x2, 1)
print("Resultado do Teste 2:", x2)

# Teste 3
A3 = np.array([[20, -1, 2, 3, 4, 6], [-6, 30, -1, -4, 3, 5], [-2, 1, 15, 1, 4, 6], [2, -2, 1, 24, 4, -1], [3, 3, -4, 7, 35, 7], [1, -3, 2, 6, 3, 27]])
b3 = np.array([1, 59, -11, -68, 9, -74], dtype=float)
x3 = gauss_seidel(A3, b3)
x3 = np.round(x3, 1)
print("Resultado do Teste 3:", x3)