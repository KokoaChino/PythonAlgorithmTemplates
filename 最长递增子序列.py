from bisect import bisect_left

def length_of_LIS(nums: list) -> int: # 最长递增子序列
    g = []
    for x in nums:
        i = bisect_left(g, x)
        if i == len(g):
            g.append(x)
        else:
            g[i] = x
    return len(g)