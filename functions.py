import math

def ackley_function(x):
    a = 20
    b = 0.2
    c = 2 * math.pi
    first_sum = sum([xi ** 2 for xi in x])
    second_sum = sum([math.cos(c * xi) for xi in x])
    d = len(x)
    first_term = -a * math.exp(-b * math.sqrt(first_sum / d))
    second_term = -math.exp(second_sum / d)
    return first_term + second_term + a + math.exp(1)


def rastrigin_function(x):
    A = 10
    d = len(x)
    return A * d + sum([(xi**2 - A * math.cos(2 * math.pi * xi)) for xi in x])


def schwefel_function(x):
    d = len(x)
    return 418.9829 * d - sum([xi * math.sin(math.sqrt(abs(xi))) for xi in x])


def rosenbrock_function(x):
    d = len(x)
    sum_term = sum([(100 * (x[i+1] - x[i]**2)**2 + (1 - x[i])**2) for i in range(d-1)])
    return sum_term