def one_difference(nums: list, operates: list) -> None: # 一维差分
    n = len(nums)
    dif = [0] * (n + 1)
    for i, j, d in operates:
        dif[i] += d
        dif[j + 1] -= d
    for i in range(n):
        dif[i + 1] += dif[i]
        nums[i] += dif[i]

def two_difference(mat: list, operates: list) -> None: # 二维差分
    n, m = len(mat), len(mat[0])
    dif = [[0] * (m + 2) for _ in range(n + 2)]
    for x1, y1, x2, y2, d in operates:
        dif[x2 + 2][y2 + 2] += d
        dif[x1 + 1][y2 + 2] -= d
        dif[x2 + 2][y1 + 1] -= d
        dif[x1 + 1][y1 + 1] += d
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dif[i][j] += dif[i - 1][j] + dif[i][j - 1] - dif[i - 1][j - 1]
            mat[i - 1][j - 1] += dif[i][j]