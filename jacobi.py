import numpy as np

def gauss_jacobi(A, b, tol=1e-6, max_iter=100):
    n = len(b)
    x = np.zeros(n)
    x_new = np.copy(x)

    for iteration in range(max_iter):
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i, j] * x[j]
            x_new[i] = (b[i] - sigma) / A[i, i]

        if np.allclose(x, x_new, atol=tol):
            print(f"Iteration {iteration + 1}: {x_new}")
            return x_new.round(decimals=1)

        x = np.copy(x_new).round(decimals=1)
        print(f"Iteration {iteration + 1}: {x}")

    print("Maximum number of iterations reached.")
    return x

# Teste 3
A3 = np.array([[20, -1, 2, 3, 4, 6], [-6, 30, -1, -4, 3, 5], [-2, 1, 15, 1, 4, 6], [2, -2, 1, 24, 4, -1], [3, 3, -4, 7, 35, 7], [1, -3, 2, 6, 3, 27]])
b3 = np.array([1, 59, -11, -68, 9, -74], dtype=float)
result3 = gauss_jacobi(A3, b3)
print("Final result:", result3)