def longest_common_subsequence(arr1: list, arr2: list) -> int: # 最长公共子序列
    ans = [0] * (len(arr2) + 1)
    for x in arr1:
        pre = 0
        for j, y in enumerate(arr2):
            pre, ans[j + 1] = ans[j + 1], pre + 1 if x == y else max(ans[j], ans[j + 1])
    return ans[-1]