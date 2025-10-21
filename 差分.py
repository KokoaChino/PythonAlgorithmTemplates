def one_difference(nums: list, operations: list) -> None: # 一维差分
    n = len(nums)
    dif = [0] * (n + 1)
    for i, j, d in operations:
        dif[i] += d
        dif[j + 1] -= d
    for i in range(n):
        dif[i + 1] += dif[i]
        nums[i] += dif[i]

def two_difference(mat: list, operations: list) -> None: # 二维差分
    n, m = len(mat), len(mat[0])
    dif = [[0] * (m + 2) for _ in range(n + 2)]
    for x1, y1, x2, y2, d in operations:
        dif[x2 + 2][y2 + 2] += d
        dif[x1 + 1][y2 + 2] -= d
        dif[x2 + 2][y1 + 1] -= d
        dif[x1 + 1][y1 + 1] += d
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dif[i][j] += dif[i - 1][j] + dif[i][j - 1] - dif[i - 1][j - 1]
            mat[i - 1][j - 1] += dif[i][j]



from typing import List
from bisect import bisect_right
from collections import defaultdict

class OneSparseDifference: # 一维稀疏差分
    def __init__(self, operations: List[List[int]]):
        dif = defaultdict(int)
        for l, r, d in operations:
            dif[l] += d
            dif[r + 1] -= d
        self._positions = [-1]
        self._values = [0]
        for pos in sorted(dif.keys()):
            self._values.append(self._values[-1] + dif[pos])
            self._positions.append(pos)

    def get(self, i: int) -> int:
        return self._values[bisect_right(self._positions, i) - 1]



class TwoSparseDifference: # 二维稀疏差分
    def __init__(self, operations: List[List[int]]):
        x_set = set()
        y_set = set()
        for x1, y1, x2, y2, d in operations:
            x_set.add(x1)
            x_set.add(x2 + 1)
            y_set.add(y1)
            y_set.add(y2 + 1)
        self.xs = sorted(x_set)
        self.ys = sorted(y_set)
        x_to_idx = {x: i for i, x in enumerate(self.xs)}
        y_to_idx = {y: i for i, y in enumerate(self.ys)}
        n, m = len(self.xs), len(self.ys)
        dif = [[0] * (m + 2) for _ in range(n + 2)]
        for op in operations:
            x1, y1, x2, y2, d = op
            i1 = x_to_idx[x1] + 1
            j1 = y_to_idx[y1] + 1
            i2 = x_to_idx[x2 + 1] + 1
            j2 = y_to_idx[y2 + 1] + 1
            dif[i1][j1] += d
            dif[i2][j1] -= d
            dif[i1][j2] -= d
            dif[i2][j2] += d
        self.g = [[0] * m for _ in range(n)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dif[i][j] += dif[i - 1][j] + dif[i][j - 1] - dif[i - 1][j - 1]
                self.g[i - 1][j - 1] = dif[i][j]

    def get(self, x: int, y: int) -> int:
        i = bisect_right(self.xs, x) - 1
        if i < 0:
            return 0
        j = bisect_right(self.ys, y) - 1
        if j < 0:
            return 0
        return self.g[i][j]