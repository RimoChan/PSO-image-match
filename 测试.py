import 粒子群匹配
import cv0


莉沫 = cv0.read('./图/莉沫.png') / 255
耳朵 = cv0.read('./图/斜小耳朵.png') / 255
best_cost, best_pos = 粒子群匹配.匹配(莉沫, 耳朵, 缩放范围=(1.3, 1.4), 旋转范围=(-3.14, 3.14))


# 画出来看看

import math
import numpy as np
from 矩阵 import 旋转矩阵

x, y, 缩放, 角 = best_pos
转 = 旋转矩阵(角)
w2, h2 = 耳朵.shape[:2]
原 = np.array([x, y])
a = np.array([h2, 0]) @ 转 * 缩放
b = np.array([0, w2]) @ 转 * 缩放
for 点1, 点2 in [
    (原, 原 + a),
    (原 + a, 原 + a + b),
    (原 + a + b, 原 + b),
    (原 + b, 原)
    ]:
    x1, y1 = int(点1[0]), int(点1[1])
    x2, y2 = int(点2[0]), int(点2[1])
    cv0.line(莉沫, (x1, y1), (x2, y2), (1, 0, 0))
cv0.show(莉沫)
