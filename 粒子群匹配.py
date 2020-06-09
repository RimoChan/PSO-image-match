import math

import pyswarms
import numpy as np

import cv0

from 矩阵 import 旋转矩阵


def 匹配(原图, 目标图, 缩放范围, 旋转范围):
    w1, h1 = 原图.shape[:2]
    w2, h2 = 目标图.shape[:2]
    def 代价(粒子群):
        def 粒子代价(x, y, 缩放, 角):
            转 = 旋转矩阵(角)
            原 = np.array([x, y])
            a = np.array([h2, 0]) @ 转 * 缩放
            b = np.array([0, w2]) @ 转 * 缩放
            原点组 = np.float32([原, 原 + a, 原 + b])
            新点组 = np.float32([[0, 0], [h2, 0], [0, w2]])
            M = cv0.getAffineTransform(原点组, 新点组)
            切片 = cv0.warpAffine(原图, M, (h2, w2))
            return np.abs(切片 - 目标图).sum() / 目标图.size
        return [粒子代价(*li) for li in 粒子群]
    options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
    bounds = (
        [0, 0, 缩放范围[0], 旋转范围[0]],
        [h1, w1, 缩放范围[1], 旋转范围[1]],
    )
    optimizer = pyswarms.single.GlobalBestPSO(n_particles=400, dimensions=4, options=options, bounds=bounds)
    best_cost, best_pos = optimizer.optimize(代价, iters=128)
    return best_cost, best_pos
