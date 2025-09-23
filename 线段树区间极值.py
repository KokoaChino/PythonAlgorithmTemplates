INF = 10 ** 18

class SegmentTreeMinMax: # 线段树，单点更新，区间求极值

    __slots__ = ("n", "maxTree", "minTree")

    def __init__(self, nums):
        self.n = len(nums)
        size = 1 << (self.n.bit_length() + 1)
        self.maxTree = [0] * size
        self.minTree = [0] * size
        self.__build__(nums, 0, self.n - 1, 1)

    def __build__(self, nums, left: int, right: int, i: int):
        if left == right:
            self.maxTree[i] = self.minTree[i] = nums[left]
            return
        mid = (left + right) >> 1
        self.__build__(nums, left, mid, 2 * i)
        self.__build__(nums, mid + 1, right, 2 * i + 1)
        self.maxTree[i] = max(self.maxTree[2 * i], self.maxTree[2 * i + 1])
        self.minTree[i] = min(self.minTree[2 * i], self.minTree[2 * i + 1])

    def __query_max__(self, start: int, end: int, left: int, right: int, i: int) -> int:
        if start <= left and right <= end:
            return self.maxTree[i]
        mid = (left + right) >> 1
        res = -INF
        if start <= mid:
            res = max(res, self.__query_max__(start, end, left, mid, 2 * i))
        if end >= mid + 1:
            res = max(res, self.__query_max__(start, end, mid + 1, right, 2 * i + 1))
        return res

    def __query_min__(self, start: int, end: int, left: int, right: int, i: int) -> int:
        if start <= left and right <= end:
            return self.minTree[i]
        mid = (left + right) >> 1
        res = INF
        if start <= mid:
            res = min(res, self.__query_min__(start, end, left, mid, 2 * i))
        if end >= mid + 1:
            res = min(res, self.__query_min__(start, end, mid + 1, right, 2 * i + 1))
        return res

    def __update__(self, index: int, val: int, left: int, right: int, i: int):
        if left == right:
            self.maxTree[i] = self.minTree[i] = val
            return
        mid = (left + right) >> 1
        if index <= mid:
            self.__update__(index, val, left, mid, 2 * i)
        else:
            self.__update__(index, val, mid + 1, right, 2 * i + 1)
        self.maxTree[i] = max(self.maxTree[2 * i], self.maxTree[2 * i + 1])
        self.minTree[i] = min(self.minTree[2 * i], self.minTree[2 * i + 1])

    def query_max(self, start: int, end: int) -> int: # 求区间极值
        if start > end:
            return 0
        return self.__query_max__(start, end, 0, self.n - 1, 1)

    def query_min(self, start: int, end: int) -> int: # 求区间极值
        if start > end:
            return 0
        return self.__query_min__(start, end, 0, self.n - 1, 1)

    def update(self, index: int, val: int): # 单点更新
        self.__update__(index, val, 0, self.n - 1, 1)