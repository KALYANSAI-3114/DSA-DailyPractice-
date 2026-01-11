#My approach

def runningSum(nums):
    n = len(nums)
    s = [0]*n
    for i in range(n):
        s[i] = sum(nums)- sum(nums[i+1:])
    return s
#Time Complexity =  O(n^2)  
#Space Complexity = O(n)    
def runningSumOptimal(nums):
    n = len(nums)
    for i in range(1,n):
        nums[i] = nums[i]+nums[i-1]

    return nums
#Time Complexity = O(n) 
#Space Complexity = O(1)