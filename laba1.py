import allfunc as af

# LU разложение
A = [[-7, 3, -4, 7], [8, -1, -7, 6], [9, 9, 3, -6], [-7, -9, -8, -5]]
U = [[-7, 3, -4, 7], [8, -1, -7, 6], [9, 9, 3, -6], [-7, -9, -8, -5]]
L = [[0 for i in range(len(A))] for j in range(len(A))]

for i in range(len(A)):
    for j in range(i, len(A)):
        L[j][i] = U[j][i] / U[i][i]

for r in range(1, len(A)):

    for i in range(r - 1, len(A)):
        for j in range(i, len(A)):
            L[j][i] = U[j][i] / U[i][i]

    for i in range(r, len(A)):
        for j in range(r - 1, len(A)):
            U[i][j] = U[i][j] - L[i][r - 1] * U[r - 1][j]

C = af.dot_mat(L, U)

for i in range(len(A)):
    for j in range(len(A)):
        print(int(C[i][j]), end=' ')
    print()

print('=')

for i in range(len(A)):
    for j in range(len(A)):
        print(A[i][j], end=' ')
    print()

# Находим определитель
det = 1
for i in range(len(A)):
    det = det * U[i][i]

print(' Определитель матрицы ', round(det))

# Находим решение СЛАУ и обратную матрицу

E = [[0 for i in range(len(A))] for j in range(len(A))]
for i in range(len(A)):
    E[i][i] = 1

z = [0 for i in range(len(A))]
b = [-126, 29, 27, 34]

z[0] = b[0]
z[1] = b[1] - L[1][0] * z[0]
for i in range(2, 4):
    s = 0
    for j in range(i - 1):
        s = s + L[i][j] * z[j]
    z[i] = b[i] - s
print('z = ', z)


x = [0 for i in range(len(A))]
x[3] = z[3] / U[3][3]
x[2] = (1 / U[2][2]) * (z[2] - U[2][3] * x[3])
for i in range(len(A) - 3, -1, -1):
    s = 0
    for j in range(i + 1, len(A)):
        s = s + U[i][j] * x[j]
    x[i] = (1 / U[i][i]) * (z[i] - s)

print('x = ', x)

X = []
X.append(x)

P = af.dot_mat(L, U)
P = af.dot_mat(P, X)

print('P = ', P)

print('b =  ', b)