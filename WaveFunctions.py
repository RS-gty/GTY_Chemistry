from QuantumChemistry import *

# Constants
a0 = 0.529


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


# 2p group
def AngleWaveFunction_2pz(theta: np.ndarray, phi: np.ndarray):
    matrix_list = []
    cosine = []
    for i in range(theta.size):
        cosine.append(np.cos(theta.tolist()[0][i]))

    for i in range(theta.size):
        matrix_list.append(np.sqrt(3 / (4 * np.pi)) * cosine[i])
    return np.array(matrix_list)


def AngleWaveFunction_2px(theta: np.ndarray, phi: np.ndarray):
    matrix_list = []
    cosine = []
    for i in range(theta.size):
        cosine.append(np.sin(theta.tolist()[0][i])*np.cos(phi.tolist()[0][i]))

    for i in range(theta.size):
        matrix_list.append(np.sqrt(3 / (4 * np.pi)) * cosine[i])
    return np.array(matrix_list)


def AngleWaveFunction_2py(theta: np.ndarray, phi: np.ndarray):
    matrix_list = []
    cosine = []
    for i in range(theta.size):
        cosine.append(np.sin(theta.tolist()[0][i])*np.sin(phi.tolist()[0][i]))

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


def AngleWaveFunction_3dxz(theta: np.ndarray, phi: np.ndarray):
    matrix_list = []
    sine1 = []
    cosine1 = []
    cosine2 = []
    for i in range(theta.size):
        sine1.append(power(1, np.sin(theta.tolist()[0][i]), 1))
    for i in range(theta.size):
        cosine1.append(power(1, np.cos(theta.tolist()[0][i]), 1))
    for i in range(phi.size):
        cosine2.append(power(1, np.cos(phi.tolist()[0][i]), 1))

    for i in range(theta.size):
        matrix_list.append(np.sqrt(5 / (4 * np.pi)) * sine1[i] * cosine1[i] * cosine2[i])

    return np.array(matrix_list)


# 4f

def RadialWaveFunction_4f(radius):
    return (1 / (768 * np.sqrt(35))) * power(1, (1 / a0), 1.5) * power(1, radius / a0, 3) * exp_(-1 * radius / (4 * a0))


def AngleWaveFunction_4fz3(theta: np.ndarray, phi: np.ndarray):
    matrix_list = []
    cosine1 = []
    cosine2 = []
    for i in range(theta.size):
        cosine1.append(power(5, np.cos(theta.tolist()[0][i]), 3))
    for i in range(theta.size):
        cosine2.append(power(3, np.cos(theta.tolist()[0][i]), 1))

    for i in (range(theta.size)):
        matrix_list.append(np.sqrt(7 / (16 * np.pi)) * (cosine1[i] - cosine2[i]))

    return np.array(matrix_list)


def AngleWaveFunction_4fxz2(theta: np.ndarray, phi: np.ndarray):
    matrix_list = []
    sine1 = []
    cosine1 = []
    cosine2 = []
    for i in range(theta.size):
        sine1.append(power(1, np.cos(theta.tolist()[0][i]), 1))
    for i in range(theta.size):
        cosine1.append(power(5, np.cos(theta.tolist()[0][i]), 2) - 1)
    for i in range(phi.size):
        cosine2.append(power(1, np.cos(phi.tolist()[0][i]), 1))

    for i in range(theta.size):
        matrix_list.append(np.sqrt(42 / (64 * np.pi)) * sine1[i] * cosine1[i] * cosine2[i])

    return np.array(matrix_list)


def AngleWaveFunction_4fx3mxy2(theta: np.ndarray, phi: np.ndarray):
    matrix_list = []
    sine1 = []
    cosine1 = []
    cosine2 = []
    for i in range(theta.size):
        sine1.append(power(1, np.cos(theta.tolist()[0][i]), 2))
    for i in range(theta.size):
        cosine1.append(power(1, np.cos(theta.tolist()[0][i]), 1))
    for i in range(phi.size):
        cosine2.append(power(1, 2 * np.cos(phi.tolist()[0][i]), 1))

    for i in range(theta.size):
        matrix_list.append(np.sqrt(105 / (16 * np.pi)) * sine1[i] * cosine1[i] * cosine2[i])

    return np.array(matrix_list)


def AngleWaveFunction_4fx3m3xy2(theta: np.ndarray, phi: np.ndarray):
    matrix_list = []
    sine1 = []
    cosine1 = []
    for i in range(theta.size):
        sine1.append(power(1, np.cos(theta.tolist()[0][i]), 3))
    for i in range(theta.size):
        cosine1.append(power(1, 3 * np.cos(phi.tolist()[0][i]), 1))

    for i in range(theta.size):
        matrix_list.append(np.sqrt(70 / (64 * np.pi)) * sine1[i] * cosine1[i])

    return np.array(matrix_list)
