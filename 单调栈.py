def last_smaller_element(nums: list) -> list: # 上一个更小元素
    n = len(nums)
    ans, stack = [-1] * n, []
    for i in range(n):
        while stack and nums[i] <= nums[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans

def last_bigger_element(nums: list) -> list: # 上一个更大元素
    n = len(nums)
    ans, stack = [-1] * n, []
    for i in range(n):
        while stack and nums[i] >= nums[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans

def next_smaller_element(nums: list) -> list: # 下一个更小元素
    n = len(nums)
    ans, stack = [n] * n, []
    for i in range(n - 1, -1, -1):
        while stack and nums[i] <= nums[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans

def next_bigger_element(nums: list) -> list: # 下一个更大元素
    n = len(nums)
    ans, stack = [n] * n, []
    for i in range(n - 1, -1, -1):
        while stack and nums[i] >= nums[stack[-1]]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(i)
    return ans