import numpy as np
from QuantumChemistry import *
# Constants
a0 = 0.529  # 52.9pm


def RadialWaveFunction_1s(radius):
    return 2 * np.sqrt(1 / power(1, a0, 3)) * np.exp(-radius / a0)


def AngleWaveFunction_1s(theta: np.ndarray, phi):
    matrix_list = []
    for i in range(theta.size):
        matrix_list.append(np.sqrt(1 / (4 * np.pi)))
    return np.array(matrix_list)


def RadialWaveFunction_2s(radius):
    return np.sqrt(1 / (8 * power(1, a0, 3))) * (2 - radius / a0) * np.exp(-radius / (2 * a0))


def RadialWaveFunction_2p(radius):
    return (1 / np.sqrt(24)) * power(1, (1 / a0), 1.5) * (radius / a0) * exp_(-1 * radius / (2 * a0))


def AngleWaveFunction_2p(theta: np.ndarray, phi):
    matrix_list = []
    cosine = []
    for i in range(theta.size):
        cosine.append(np.cos(theta.tolist()[0][i]))

    for i in range(theta.size):
        matrix_list.append(np.sqrt(3 / (4 * np.pi)) * cosine[i])
    return np.array(matrix_list)


def RadialWaveFunction_3d(radius):
    return (4 / (81 * np.sqrt(30))) * power(1, (1 / a0), 1.5) * (power(1, radius, 2) / power(1, a0, 2) *
                                                                 exp_(-1 * radius / (3 * a0)))


def AngleWaveFunction_3dz2(theta: np.ndarray, phi: np.ndarray):
    matrix_list = []
    cosine = []
    for i in range(theta.size):
        cosine.append(power(3, np.cos(theta.tolist()[0][i]), 2) - 1)

    for i in range(theta.size):
        matrix_list.append(np.sqrt(5 / (16 * np.pi)) * cosine[i])
    return np.array(matrix_list)
