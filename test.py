import math

import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from WaveFunctions import *
from scipy.special import genlaguerre
import matplotlib.pyplot as plt
import numpy.fft
from scipy.misc import derivative


def GenerateRadialWaveFunction(n: int, l: int, radius: np.ndarray, a0_=0.529):
    matrix_list = []
    coefficient1 = np.sqrt(power(1, 2 / (a0_ * n), 3) * (math.factorial(n - l - 1) / math.factorial(2 * n * (n + l))))
    for rad in radius:
        coefficient2 = power(1, (2 * rad) / (n * a0_), l) * np.exp((-1 * rad) / (n * a0_))
        coefficient3 = genlaguerre(n - l - 1, 2 * l + 1)(rad)
        coefficient4 = (2 * rad) / (n * a0_)
        matrix_list.append(coefficient1 * coefficient2 * coefficient3 * coefficient4)
    return np.array(matrix_list)


def sum_(func, x0, x1, diff):
    xrange = np.arange(x0, x1, diff)
    yrange = func(xrange)
    temp = 0
    for i in range(len(xrange) - 1):
        temp += diff * (yrange[i] + yrange[i + 1]) / 2

    return temp


def func1(x0: np.ndarray) -> int:
    return 4 * np.pi * x0 ** 2 * GenerateRadialWaveFunction(1, 0, x0) ** 2


def func2(x0: np.ndarray) -> int:
    return 4 * np.pi * x0 ** 2 * GenerateRadialWaveFunction(2, 0, x0) ** 2


def func3(x0: np.ndarray) -> int:
    return 4 * np.pi * x0 ** 2 * GenerateRadialWaveFunction(3, 0, x0) ** 2


def func4(x0: np.ndarray) -> int:
    return 4 * np.pi * x0 ** 2 * GenerateRadialWaveFunction(4, 0, x0) ** 2


if __name__ == '__main__':
    delta = 0.01
    # 生成代表X轴数据的列表
    x = np.arange(0, 16 * np.pi, delta)
    y0 = func1(x) / sum_(func1, 0, 20, 0.1)
    y1 = func2(x) / sum_(func2, 0, 20, 0.1)
    y2 = func3(x) / sum_(func3, 0, 20, 0.1)
    y3 = func4(x) / sum_(func4, 0, 20, 0.1)

    plt.plot(x, y0)
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.plot(x, y3)
    plt.show()
