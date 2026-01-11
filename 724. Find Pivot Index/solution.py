
#My Approach
def pivotIndex(nums):
    leftSum = 0
    n = len(nums)
    for i in range(n):
        if leftSum == sum(nums[i+1:]):
            return i
        leftSum = sum(nums[:i+1])

    return -1
#Time Complexity = O(n^2)
#Space Complexity = O(1)


#Optimal Approach
def pivot(nums):
    totalSum = sum(nums)
    leftSum = 0
    for i in range(len(nums)):
        if leftSum == totalSum-leftSum-nums[i]:
            return i 
        leftSum += nums[i]
    return -1


#Time Complexity = O(n)
#Space Complexity = O(1)
nums1 = [1,7,3,6,5,6]
nums2 = [1,2,3]

print(pivotIndex(nums1))
print(pivot(nums2))