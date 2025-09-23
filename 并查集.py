class UnionFindSet: # 并查集

    __slots__ = ("n", "fa", "size", "cnt")

    def __init__(self, n: int):
        self.n = n
        self.fa = list(range(n))
        self.size = [1] * n
        self.cnt = n

    def find(self, x: int) -> int: # 查找元素 x 所在集合的代表元素
        ans, fa = x, self.fa
        while fa[ans] != ans:
            ans = fa[ans]
        while fa[x] != ans:
            fa[x], x = ans, fa[x]
        return ans

    def merge(self, i: int, j: int): # 合并元素 i 和 j 所在的集合
        fa, size = self.fa, self.size
        x, y = self.find(i), self.find(j)
        if x == y:
            return
        if size[x] > size[y]:
            x, y = y, x
        fa[x] = y
        size[y] += size[x]
        self.cnt -= 1

    def is_same(self, i: int, j: int) -> bool: # 判断元素 i 和 j 是否属于同一集合
        return self.find(i) == self.find(j)

    def get_size(self, x: int) -> int: # 查询元素 x 所在集合的元素个数
        return self.size[self.find(x)]

    def get_cnt(self) -> int: # 查询不同集合的个数
        return self.cnt