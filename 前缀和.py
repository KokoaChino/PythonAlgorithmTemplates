class OnePrefixProd: # 一维前缀积
    def __init__(self, nums: list):
        p = [1] * (len(nums) + 1)
        for i, v in enumerate(nums):
            p[i + 1] = p[i] * v
        self.P = p

    def get_prod(self, i: int, j: int) -> int: # 区间求积
        return self.P[j + 1] // self.P[i]



class OnePrefixSum: # 一维前缀和
    def __init__(self, nums: list):
        p = [0] * (len(nums) + 1)
        for i, v in enumerate(nums):
            p[i + 1] = p[i] + v
        self.P = p

    def get_sum(self, i: int, j: int) -> int: # 区间求和
        return self.P[j + 1] - self.P[i]



class TwoPrefixSum: # 二维前缀和
    def __init__(self, mat: list):
        n, m = len(mat), len(mat[0])
        p = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                p[i + 1][j + 1] = p[i][j + 1] + p[i + 1][j] - p[i][j] + mat[i][j]
        self.P = p

    def get_sum(self, x1: int, y1: int, x2: int, y2: int) -> int: # 区域求和
        P = self.P
        return P[x2 + 1][y2 + 1] - P[x1][y2 + 1] - P[x2 + 1][y1] + P[x1][y1]