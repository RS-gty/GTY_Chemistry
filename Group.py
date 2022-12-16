import matplotlib.pyplot as plt
import numpy as np
from numpy import *
from mpl_toolkits import mplot3d
import random

# Presets
ax = plt.axes(projection='3d')


def randomcolor():
    colorArr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    color = ""
    for i in range(6):
        color += colorArr[random.randint(0, 14)]
    return "#" + color


class Group(object):
    def __init__(self):
        self.vectors = []

    def register(self, *v: ndarray):
        for i in v:
            self.vectors.append(i)

    def display(self):
        temp = []
        color_p = randomcolor()
        for i in self.vectors:
            for j in range(len(i)):
                temp.append(i[j])
            ax.quiver(0, 0, 0, temp[0], temp[1], temp[2], arrow_length_ratio=0.1, color=color_p)
            ax.scatter3D(temp[0], temp[1], temp[2], color=color_p, s=2500)
            temp = []

    def rotate(self, theta: 2 * pi):
        rotation_matrix = array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], [0, 0, 1]])
        for i in range(len(self.vectors)):
            self.vectors[i] = dot(rotation_matrix, self.vectors[i])


def initial():
    x = np.arange(-6, 6, 0.1)
    y = np.zeros(120)

    ax.plot(x, y, y, color='#000000')
    ax.plot(y, x, y, color='#000000')
    ax.plot(y, y, x, color='#000000')

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    plt.gca().set_box_aspect((1, 1, 1))

    plt.show()


def main():
    a1 = array([[1], [1], [1]])
    a2 = array([[-1], [-1], [1]])
    a3 = array([[1], [-1], [-1]])
    a4 = array([[-1], [1], [-1]])

    G1 = Group()
    G1.register(a1, a2, a3, a4)

    G1.display()
    G1.rotate(pi / 2)
    G1.display()

    initial()


if __name__ == '__main__':
    main()
