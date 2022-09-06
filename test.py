import base64

import numpy as np
from numpy import linalg
from scipy.linalg import sqrtm
from CHEM import *

a = np.matrix([[1.0, 4.0, 6.0], [4.0, 20.0, 34.0], [6.0, 34.0, 70.0]])
b = np.matrix([[1, 0, 0, 0], [5, 2, 0, 0], [8, 6, 3, 0], [10, 9, 7, 4]])


def GetRange(i: int, j: int) -> list:
    ran = []
    for n in range(i, j+1):
        ran.append(n)
    if i > j:
        return [None]
    elif i == j:
        return [i]
    else:
        return ran


def IsSymmetryPositiveDefiniteMatrix(matrix: np.ndarray):
    if np.array_equal(matrix, matrix.T):
        try:
            np.linalg.cholesky(matrix)
            return True
        except np.linalg.LinAlgError:
            return False
    else:
        return False


def Cal1(l1):
    return [abs(l1[0]-l1[1]), abs(l1[1]-l1[2]), abs(l1[2]-l1[3]), abs(l1[3]-l1[0])]


if __name__ == '__main__':
    b = bytes('abcdefgh'.encode('utf-8'))
    print(bytes('abcdefgh'.encode('utf-8')))
    print(str(b))

