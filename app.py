import pandas as pd
import math

def function(x):
    result = x**3 - 9*x + 3
    return result

def bisection(a, b, tol):
    results = []
    step = 1

    while abs(b - a) > tol:
        c = (a + b) / 2
        fa = function(a)
        fb = function(b)
        fc = function(c)
        error_margin = abs(c - a)

        results.append([step, a, b, c, fa, fb, fc, error_margin])
    
        if fa * fc < 0:
            b = c
        else:
            a = c

        step += 1

    decimal_places = 3
    df = pd.DataFrame(results, columns=["k", "a", "b", "x", "f(a)", "f(b)", "f(x)", "|xk+1 - xk|"])
    df = df.round(decimals=decimal_places)
    return df

def false_position(a, b, tol):
    results = []
    step = 1

    while abs(b - a) > tol:
        fa = function(a)
        fb = function(b)
        c = (a * fb - b * fa) / (fb - fa)
        fc = function(c)
        error_margin = abs(c - a)

        results.append([step, a, b, c, fa, fb, fc, error_margin])

        if fa * fc < 0:
            b = c
        else:
            a = c

        step += 1

    decimal_places = 3
    df = pd.DataFrame(results, columns=["k", "a", "b", "x", "f(a)", "f(b)", "f(x)", "|xk+1 - xk|"])
    df = df.round(decimals=decimal_places)
    return df

def fixed_point_iteration(x0, tol, max_iter):
    results = []
    step = 1

    while step <= max_iter:
        x1 = x0 - (x0**3 - 9*x0 + 3) / (3*x0**2 - 9)
        error_margin = abs(x1 - x0)
        
        results.append([step, x0, x1, error_margin])

        if error_margin < tol:
            break

        x0 = x1
        step += 1

    decimal_places = 3
    df = pd.DataFrame(results, columns=["k", "xk", "xk+1", "|xk+1 - xk|"])
    df = df.round(decimals=decimal_places)
    return df

def newton_raphson(x0, tol, max_iter):
    results = []
    step = 1

    while step <= max_iter:
        fx0 = function(x0)
        dfx0 = 3 * x0**2 - 9
        x1 = x0 - fx0 / dfx0
        error_margin = abs(x1 - x0)

        results.append([step, x0, fx0, dfx0, x1, error_margin])

        if error_margin < tol:
            break

        x0 = x1
        step += 1

    decimal_places = 3
    df = pd.DataFrame(results, columns=["k", "xk", "f(xk)", "f'(xk)", "xk+1", "|xk+1 - xk|"])
    df = df.round(decimals=decimal_places)
    return df

tolerance = 1e-5
initial_interval = [0, 1]
initial_guess = 0.5
max_iterations = 30

# Bisection
bisection_df = bisection(initial_interval[0], initial_interval[1], tolerance)
print("Bisection Method:")
print(bisection_df)

# False Position
false_position_df = false_position(initial_interval[0], initial_interval[1], tolerance)
print("\nFalse Position Method:")
print(false_position_df)

# Fixed-Point Iteration
fixed_point_df = fixed_point_iteration(initial_guess, tolerance, max_iterations)
print("\nFixed-Point Iteration Method:")
print(fixed_point_df)

# Newton-Raphson
newton_raphson_df = newton_raphson(initial_guess, tolerance, max_iterations)
print("\nNewton-Raphson Method:")
print(newton_raphson_df)