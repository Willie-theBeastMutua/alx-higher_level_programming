#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_cp = [i.copy() for i in matrix]
    leng = len(matrix)
    for i in range(leng):
        leng_in = len(matrix[i])
        for j in range(leng_in):
            val = matrix[i][j] * matrix[i][j]
            matrix_cp[i][j] = val
    return matrix_cp
