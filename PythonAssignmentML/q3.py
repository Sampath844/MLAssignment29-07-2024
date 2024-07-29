def matrix_multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_power(A, m):
    n = len(A)

    result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]

    base = A

    while m > 0:
        if m % 2 == 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        m //= 2

    return result

A = [[4, 5],
     [6, 7]]
m = 2

result = matrix_power(A, m)
for row in result:
    print(row)