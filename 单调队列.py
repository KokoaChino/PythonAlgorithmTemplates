from collections import deque

def min_sliding_window(nums: list, k: int) -> list: # 滑动窗口最小值
    n = len(nums)
    ans = [0] * n
    q = deque()
    for i in range(n - 1, -1, -1):
        max_index = min(i + k - 1, n - 1)
        if q and q[0] > max_index:
            q.popleft()
        while q and nums[i] <= nums[q[-1]]:
            q.pop()
        q.append(i)
        ans[i] = nums[q[0]]
    return ans

def max_sliding_window(nums: list, k: int) -> list: # 滑动窗口最大值
    n = len(nums)
    ans = [0] * n
    q = deque()
    for i in range(n - 1, -1, -1):
        max_index = min(i + k - 1, n - 1)
        if q and q[0] > max_index:
            q.popleft()
        while q and nums[i] >= nums[q[-1]]:
            q.pop()
        q.append(i)
        ans[i] = nums[q[0]]
    return ans