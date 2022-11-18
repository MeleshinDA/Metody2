import math


def dichotomy_method(a, b, error_lim, func_to_calculate):  # 2.474781036376953, 10
    c = 0
    n = 0
    while abs(b - a) > error_lim:
        c = (a + b) / 2

        if func_to_calculate(c) * func_to_calculate(a) < 0:
            b = c
            continue

        a = c
        n += 1
    return c, n


def newton_method(x0, error_lim):  # 2.4747830916692064, 4
    xn = x0
    xnp1 = xn - function_did(xn) / func_derivative(xn)
    counter = 0
    while abs(xnp1 - xn) > error_lim:
        xn = xnp1
        xnp1 = xnp1 - function_did(xnp1) / func_derivative(xnp1)
        counter += 1

    return xnp1, counter


def newton_method_mod(x0, error_lim):  # 2.4747746586860697, 26
    xn = x0
    func_derivative_res = func_derivative(x0)
    xnp1 = xn - function_did(xn) / func_derivative_res
    counter = 0
    while abs(xnp1 - xn) > error_lim:
        xn = xnp1
        xnp1 = xnp1 - function_did(xnp1) / func_derivative_res
        counter += 1

    return xnp1, counter


def chordes_method(x0, x1, error_lim):  # 2.474784632561717, 14
    xn = x0
    xnp1 = x1
    counter = 0
    while abs(xnp1 - xn) > error_lim:
        xn = xnp1
        xnp1 = xnp1 - function_did(xnp1) * (xnp1 - x0) / (function_did(xnp1) - function_did(x0))
        counter += 1

    return xnp1, counter


def moving_chordes_method(x0, x1, error_lim):  # 2.474783091736477, 5
    xnm1 = x0
    xn = x1
    xnp1 = xn - function_did(xn) * (xn - xnm1) / (function_did(xn) - function_did(xnm1))
    counter = 0
    while abs(xnp1 - xn) > error_lim:
        xnm1 = xn
        xn = xnp1
        xnp1 = xn - function_did(xn) * (xn - xnm1) / (function_did(xn) - function_did(xnm1))
        counter += 1
    return xnp1, counter


def simple_iteration_method(x0, error_lim): # 2.474790042129412, 38
    xn = x0
    xnp1 = phi_function(x0)
    counter = 0
    while abs(xnp1 - xn) > error_lim:
        xn = xnp1
        xnp1 = phi_function(xn)
        counter += 1
    return xnp1, counter


def func_derivative(x):
    a = 1 / (math.cos(x) * math.cos(x))
    b = 2 / (math.log(10) * x)
    return a + b


def func_derivative_2(x):
    a = 2 * math.sin(x) / (math.cos(x) ** 3)
    b = 2 / (math.log(10) * x ** 2)
    return a - b


def phi_function(x):
    log_val = -2 * math.log(x, 10)
    val = math.atan(log_val)
    return val


def function_did(x):
    a = math.tan(x)
    b = math.log(x, 10)
    return a + 2 * b


if __name__ == '__main__':
    print(dichotomy_method(2, 3, 0.5e-5, function_did))
    print(newton_method(2, 0.5e-5))
    print(newton_method_mod(2, 0.5e-5))
    print(chordes_method(2, 3, 0.5e-5))
    print(moving_chordes_method(2, 3, 0.5e-5))
    print(simple_iteration_method(2, 0.5e-5))
