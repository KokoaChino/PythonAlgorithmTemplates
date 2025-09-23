def or_list(nums: list) -> set: # 返回按位或的结果集
    ans = set(nums)
    for i, x in enumerate(nums):
        for j in range(i - 1, -1, -1):
            if nums[j] | nums[i] == nums[j]:
                break
            nums[j] |= nums[i]
            ans.add(nums[j])
    return ans

def and_list(nums: list) -> set: # 返回按位与的结果集
    ans = set(nums)
    for i, x in enumerate(nums):
        for j in range(i - 1, -1, -1):
            if nums[j] & nums[i] == nums[j]:
                break
            nums[j] &= nums[i]
            ans.add(nums[j])
    return ans