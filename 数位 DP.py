from functools import cache

def digitalDP(n: int) -> int: # 数位 DP 通用模板
    s = str(n)

    @cache
    def dfs(i: int, is_limit: bool, is_num: bool) -> int:
        if i == len(s):
            return int(is_num)
        ret = 0 if is_num else dfs(i + 1, False, False)
        up = int(s[i]) if is_limit else 9
        for j in range(1 - int(is_num), up + 1):
            ret += dfs(i + 1, j == up and is_limit, True)
        return ret
    
    return dfs(0, True, False)