def findMiddleIndex(nums):
    n = len(nums)

    for i in range(n):
        if sum(nums[:i]) == sum(nums[i + 1:]):
            return i
    return - 1
nums = [2,3,-1,8,4]

print(findMiddleIndex(nums))