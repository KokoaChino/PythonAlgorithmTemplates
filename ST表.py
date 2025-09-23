class SparseTable: # ST 表，静态区间极值查询

    __slots__ = ("n", "max_table", "min_table", "log")

    def __init__(self, nums: list):
        self.n = len(nums)
        if self.n == 0:
            self.max_table = self.min_table = []
            self.log = [0]
            return
        logn = self.n.bit_length()
        self.max_table = [[0] * logn for _ in range(self.n)]
        self.min_table = [[0] * logn for _ in range(self.n)]
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
        for i in range(self.n):
            self.max_table[i][0] = self.min_table[i][0] = nums[i]
        for j in range(1, logn):
            step = 1 << j
            for i in range(self.n - step + 1):
                self.max_table[i][j] = max(self.max_table[i][j - 1], self.max_table[i + (1 << (j - 1))][j - 1])
                self.min_table[i][j] = min(self.min_table[i][j - 1], self.min_table[i + (1 << (j - 1))][j - 1])

    def query_max(self, l: int, r: int) -> int:
        if l > r:
            return 0
        length = r - l + 1
        k = self.log[length]
        return max(self.max_table[l][k], self.max_table[r - (1 << k) + 1][k])

    def query_min(self, l: int, r: int) -> int:
        if l > r:
            return 0
        length = r - l + 1
        k = self.log[length]
        return min(self.min_table[l][k], self.min_table[r - (1 << k) + 1][k])