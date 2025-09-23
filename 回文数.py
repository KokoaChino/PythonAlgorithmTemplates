def get_array(U: int) -> list: # 返回所有位于 [1, 10 ^ U] 内的回文数
    ans = []
    base = 1
    while base <= 10 ** ((U - 1) // 2):
        for i in range(base, base * 10):
            x, t = i, i // 10
            while t:
                x = x * 10 + t % 10
                t //= 10
            ans.append(x)
        if base <= 10 ** (U // 2 - 1):
            for i in range(base, base * 10):
                x = t = i
                while t:
                    x = x * 10 + t % 10
                    t //= 10
                ans.append(x)
        base *= 10
    return ans