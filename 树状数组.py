class BinaryIndexedTrees: # 树状数组

    __slots__ = ("n", "d")

    def __init__(self, nums: list):
        self.n = len(nums) + 1
        self.d = [0] * self.n
        for i, v in enumerate(nums):
            self.update(i, v)
    
    def query(self, i: int, j = -1) -> int: # 区间查询
        if j < 0:
            ans = 0
            i += 1
            while i > 0:
                ans += self.d[i]
                i &= i - 1
            return ans
        else:
            return self.query(j) - self.query(i - 1)    
    
    def update(self, i: int, k: int): # 单点修改
        i += 1
        while i < self.n:
            self.d[i] += k
            i += i & -i