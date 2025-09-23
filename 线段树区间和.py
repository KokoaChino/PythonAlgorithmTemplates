class SegmentTree: # 线段树

    __slots__ = ("n", "d", "lazy")
    
    def __init__(self, nums):
        self.n = len(nums)
        self.d = [0] * (1 << (self.n.bit_length() + 1))
        self.lazy = self.d.copy()
        self.__build__(nums, 0, self.n - 1, 1)
    
    def __build__(self, nums, left: int, right: int, i: int): # 建树
        if left == right:
            self.d[i] = nums[left]
            return
        mid = (left + right) >> 1
        self.__build__(nums, left, mid, 2 * i)
        self.__build__(nums, mid + 1, right, 2 * i + 1)
        self.d[i] = self.d[2 * i] + self.d[2 * i + 1]
    
    def __query__(self, start: int, end: int, left: int, right: int, i: int) -> int: # 区间查询
        if left >= start and right <= end:
            return self.d[i]
        ret, mid = 0, (left + right) >> 1
        if self.lazy[i] and left != right:
            self.d[2 * i] += (mid - left + 1) * self.lazy[i]
            self.d[2 * i + 1] += (right - mid) * self.lazy[i]
            self.lazy[2 * i] += self.lazy[i]
            self.lazy[2 * i + 1] += self.lazy[i]
            self.lazy[i] = 0
        if start <= mid:
            ret += self.__query__(start, end, left, mid, 2 * i)
        if end >= mid + 1:
            ret += self.__query__(start, end, mid + 1, right, 2 * i + 1)
        return ret

    def __update__(self, start: int, end: int, k: int, left: int, right: int, i: int): # 区间修改
        if left >= start and right <= end:
            self.d[i] += (right - left + 1) * k
            self.lazy[i] += k
            return
        mid = (left + right) >> 1
        if self.lazy[i] and left != right:
            self.d[2 * i] += (mid - left + 1) * self.lazy[i]
            self.d[2 * i + 1] += (right - mid) * self.lazy[i]
            self.lazy[2 * i] += self.lazy[i]
            self.lazy[2 * i + 1] += self.lazy[i]
            self.lazy[i] = 0
        if start <= mid:
            self.__update__(start, end, k, left, mid, 2 * i)
        if end >= mid + 1:
            self.__update__(start, end, k, mid + 1, right, 2 * i + 1)
        self.d[i] = self.d[2 * i] + self.d[2 * i + 1]
    
    def query(self, start: int, end: int) -> int: # 区间查询
        return self.__query__(start, end, 0, self.n - 1, 1)
    
    def update(self, start: int, end: int, k: int): # 区间修改
        self.__update__(start, end, k, 0, self.n - 1, 1)