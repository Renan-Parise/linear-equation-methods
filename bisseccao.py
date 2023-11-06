import pandas as pd
import math

def setDecimal():
    return 3

def function(x):
    result = x**3 - 9 * x + 3
    # result = 1 - x * math.log(x)
    # result = 2**x - 3 * x
    # result = x**3 + x - 1000
    # result = math.exp(x) - x - 2
    # result = 2 * x - math.sin(x)
    return result

casasDecimal = setDecimal()

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

    df = pd.DataFrame(results, columns=["k", "a", "b", "x", "f(a)", "f(b)", "f(x)", "|xk+1 - xk|"])
    df = df.round(decimals=casasDecimal)
    return df

def positionFalse(a, b, tol):
    results = []
    step = 1

    while abs(b - a) > tol:
        fa = function(a)
        fb = function(b)
        
        if abs(fb - fa) < 1e-10:
            break
        
        c = (a * fb - b * fa) / (fb - fa)
        fc = function(c)
        error_margin = abs(c - a)

        results.append([step, a, b, c, fa, fb, fc, error_margin])

        if fa * fc < 0:
            b = c
        else:
            a = c

        step += 1

    df = pd.DataFrame(results, columns=["k", "a", "b", "x", "f(a)", "f(b)", "f(x)", "|xk+1 - xk|"])
    df = df.round(decimals=casasDecimal)
    return df

def fixedIteration(x0, tol, max_iter):
    results = []
    step = 1

    while step <= max_iter:
        x1 = (x0**3 + 3) / 9
        error_margin = abs(x1 - x0)
        
        results.append([step, x0, x1, error_margin])

        if error_margin < tol:
            break

        x0 = x1
        step += 1

    df = pd.DataFrame(results, columns=["k", "xk", "xk+1", "|xk+1 - xk|"])
    df = df.round(decimals=casasDecimal)
    return df

def newton(x0, tol, max_iter):
    results = []
    step = 1

    while step <= max_iter:
        fx0 = function(x0)
        dfx0 = 3 * x0**2 - 9
        x1 = x0 - fx0 / dfx0
        error_margin = abs(x1 - x0)

        results.append([step, x0, x1, error_margin])

        if error_margin < tol:
            break

        x0 = x1
        step += 1

    df = pd.DataFrame(results, columns=["k", "xk", "xk+1", "|xk+1 - xk|"])
    df = df.round(decimals=casasDecimal)
    return df

tolerance = 1e-5
init = [0, 1] # x**3 - 9 * x + 3
# init = [1, 2] # result = 1 - x * math.log(x)
# init = [1, 3] # result = 2**x - 3 * x
# init = [5, 7] # x**3 + x - 1000
# init = [0, 3] # math.exp(x) - x - 2
# init = [0, 2] # 2 * x - math.sin(x)
guessInicial = 0.5
iterMax = 30

dfBisection = bisection(init[0], init[1], tolerance)
print("Método de Bissecção:")
print(dfBisection)
print("\nEsse acaba quando o valor de xk+1 - xk é totalmente 0.\n")

dfPosition = positionFalse(init[0], init[1], tolerance)
print("\nMétodo da posição falsa:")
print(dfPosition)
print("\nEsse acaba quando o valor de xk+1 - xk começa a repetir.\n")

dfFixed = fixedIteration(guessInicial, tolerance, iterMax)
print("\nMétodo de iteração do ponto fixo:")
print(dfFixed)

dfNewton = newton(guessInicial, tolerance, iterMax)
print("\nMétodo de Newton-Raphson:")
print(dfNewton)