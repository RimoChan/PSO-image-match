from math import sin, cos

import numpy as np


def 旋转矩阵(r):
    return np.array([
        [cos(r), sin(r)],
        [-sin(r), cos(r)],
    ])
