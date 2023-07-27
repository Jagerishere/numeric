def dot_mat(a, b):  # перемножение матриц
    if len(a[0]) == len(b):
        c = [[0 for i in range(len(b[0]))] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                s = 0
                for r in range(len(a)):
                    s = s + a[i][r] * b[r][j]
                c[i][j] = s
    else:
        if len(b[0]) == len(a):
            c = [[0 for i in range(len(a[0]))] for j in range(len(b))]
            for i in range(len(b)):
                for j in range(len(a[0])):
                    s = 0
                    for r in range(len(b)):
                        s = s + b[i][r] * a[r][j]
                    c[i][j] = s
        else:
            print('Error')
            return 0
    return c
