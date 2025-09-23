from random import randint

class StringHash: # 字符串哈希

    BASE, MOD = randint(8 * 10 ** 8, 9 * 10 ** 8), 1070777777

    def __init__(self, s: str):
        n = len(s)
        BASE, MOD = StringHash.BASE, StringHash.MOD
        self.pow_base, self.pre_hash = [1] * (n + 1), [0] * (n + 1)
        for i, c in enumerate(s):
            self.pow_base[i + 1] = self.pow_base[i] * BASE % MOD
            self.pre_hash[i + 1] = (self.pre_hash[i] * BASE + ord(c)) % MOD

    def sub_hash(self, l: int, r: int) -> int: # 计算子字符串的哈希值
        return (self.pre_hash[r + 1] - self.pre_hash[l] * self.pow_base[r - l + 1]) % StringHash.MOD