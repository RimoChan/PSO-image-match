import numpy as np


def 匹配(原图, 目标图):
    w1, h1 = 原图.shape[:2]
    w2, h2 = 目标图.shape[:2]
    代价图 = np.zeros([w1 - w2 + 1, h1 - h2 + 1], dtype=np.float32)
    for x in range(w1 - w2 + 1):
        for y in range(h1 - h2 + 1):
            切片 = 原图[x:x + w2, y:y + h2]
            代价 = np.abs(切片 - 目标图).sum() / 目标图.size
            代价图[x, y] = 代价
    位置 = np.argwhere(代价图 == np.min(代价图)).tolist()
    return 位置
