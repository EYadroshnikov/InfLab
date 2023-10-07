import math


def f(a, b, c):
    return f'{(a / b) * math.sqrt((((c - 1) ** 2) / (5.4 * b)) + ((0.015 * (c - 1)) / (5.4 * a)) - 1 + c):.5E}'


A = 10**3
B = 33.3
C = 2.1

print(f(A, B, C))
