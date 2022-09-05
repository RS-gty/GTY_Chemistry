# Author:RS-gty

import random as r
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


# Calculating
def rand(row: int, column: int) -> np.ndarray:
    """
    Generate a matrix with random floats from 0 to 1
    :param row: row of the matrix
    :param column: column of the matrix
    :return: the matrix
    """
    num = row * column
    matrix_list = []
    column_list = []
    for i in range(num):
        n = i + 1
        column_list.append(r.random())
        if n % column == 0:
            matrix_list.append(column_list)
            column_list = []
        else:
            pass
    return np.array(matrix_list)


def power(x: int, b, n: int):
    """
    :return: a * b ^ n
    """
    if type(b) == np.ndarray:
        matrix_list = []
        for i in b:
            matrix_list.append(x * i ** n)
        return np.array(matrix_list)
    else:
        return x * b ** n


def exp_(matrix: np.ndarray):
    matrix_list = []
    for i in matrix:
        matrix_list.append(np.exp(i))
    return np.array(matrix_list)


def find(matrix1: np.ndarray, matrix2: np.ndarray):
    matrix_list = []
    for i in range(len(matrix1[0])):
        if matrix1[0][i] > matrix2[0][i]:
            matrix_list.append(matrix1[0][i])
    return np.array(matrix_list)


def SphericalTo3DAxis(array: np.ndarray):
    """
    change coordinate in a Spherical coordinate system into 3D-axis
    :param array: in the order of radius, theta and phi
    :return: an array that contains x, y, z coordinate in a 3D-axis
    """
    radius = array[0]
    theta = array[1]
    phi = array[2]
    x = radius * np.sin(theta) * np.cos(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(theta)
    return np.array([x, y, z])


def SphericalTo3DAxis_Matrix(array: list):
    """
    change coordinate in a Spherical coordinate system into 3D-axis
    :param array: in the order of radius, theta and phi
    :return: an array that contains x, y, z coordinate in a 3D-axis
    """
    radius = array[0]
    theta = array[1]
    phi = array[2]
    rad = []
    the = []
    ph = []
    for i in range(len(radius)):
        rad.append(float(radius[i]) * np.sin(theta[i]) * np.cos(phi[i]))
        the.append(float(radius[i]) * np.sin(theta[i]) * np.sin(phi[i]))
        ph.append(float(radius[i]) * np.cos(theta[i]))
    return [np.array(rad), np.array(the), np.array(ph)]


# Wave Functions
def RadialWaveFunction_1s(radius):
    return 2 * np.sqrt(1 / power(1, 0.529, 3)) * np.exp(-radius / 0.529)


def AngleWaveFunction_1s(theta, phi):
    return np.sqrt(1 / 4 * np.pi)


if __name__ == '__main__':
    """
    dmax = 1.1
    r0 = 2.5
    a = 0.529
    s = power(2, 10, 6)  # 2 * 10 ^ 7 采样点数
    r_sampled = r0 * rand(1, s)
    d_sampled = dmax * rand(1, s)
    distance = (4 / power(1, a, 3)) * (power(1, r_sampled, 2)) * exp_(-2 * r_sampled / a)
    q = find(distance, d_sampled)
    m = len(q)
    t = 2 * np.pi * rand(1, m)

    plt.scatter(q * np.sin(t), q * np.cos(t), s=0.00001)
    plt.show()

    print(SphericalTo3DAxis(np.array([np.sqrt(3), np.pi / 2 - np.arctan(np.sqrt(2) / 2), np.pi / 4])))
    """
    a = np.arange(0, 4, 0.00005)
    b = RadialWaveFunction_1s(a)
    c = 200000
    r_sampled = 2.5 * rand(1, c)
    theta = rand(1, c) * 2 * np.pi
    phi = rand(1, c) * 2 * np.pi

    F = SphericalTo3DAxis_Matrix([r_sampled[0].tolist(), theta.tolist()[0], phi.tolist()[0]])
    f = np.array(F)

    ax = plt.axes(projection='3d')
    ax.scatter3D(f[0], f[1], f[2], 'gray', s=0.00001)
    ax.set_title('3D line plot')
    plt.show()
