# Author:RS-gty

import random as r
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from WaveFunctions import *


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


def power(x: int, b, n):
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
    for i in range(len(radius[0])):
        rad.append(float(radius[0][i]) * np.sin(theta[0][i]) * np.cos(phi[0][i]))
        the.append(float(radius[0][i]) * np.sin(theta[0][i]) * np.sin(phi[0][i]))
        ph.append(float(radius[0][i]) * np.cos(theta[0][i]))
    return [np.array(rad), np.array(the), np.array(ph)]


def matrix_abs(a: np.ndarray):
    matrix_list = []
    for i in a:
        matrix_list.append(abs(i))
    return np.array(matrix_list)


if __name__ == '__main__':
    sample_number = 1000

    sample = rand(1, sample_number) * 10
    sample_theta = rand(1, sample_number) * 2 * np.pi
    sample_phi = rand(1, sample_number) * 2 * np.pi

    sample_y = RadialWaveFunction_3d(sample) ** 2
    sample_angle = AngleWaveFunction_3dz2(sample_theta, sample_phi)
    sample_radius = np.multiply(sample_y, sample_angle)

    t_c = SphericalTo3DAxis_Matrix([matrix_abs(sample_radius).tolist(), sample_theta.tolist(), sample_phi.tolist()])

    ax = plt.axes(projection='3d')
    ax.scatter3D(t_c[0], t_c[1], t_c[2], s=0.1, c=sample_y, cmap='cool')
    plt.show()
