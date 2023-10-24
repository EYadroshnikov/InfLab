from random import randint


def rand_matrix(n, m):
    return [[randint(0, 100) for _ in range(m)] for _ in range(n)]


def sum_of_matrix(matrix):
    sm = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            sm += matrix[i][j]
    return sm


def minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def Laplace_determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    elif n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        det = 0
        for j in range(n):
            det += ((-1) ** j) * matrix[0][j] * Laplace_determinant(minor(matrix, 0, j))
        return det


n = 3
m = 4

a = rand_matrix(n, m)
b = rand_matrix(n, n)

# 1
print('task1:')

for i in a:
    print(*i)
print()
print(f'sum of matrix: {sum_of_matrix(a)} \n   ---------')

# 2
print('task2:')
for i in b:
    print(*i)
print()
print(f'determinant: {Laplace_determinant(b)}')

