# Wap to return indices of two numbers such that they adds upto target
class Solution:
    def twoSum(self, nums, target):
        lst=[]
        i=0
        while i<len(nums):
            j=i+1
            while j<len(nums):
                if nums[i] + nums[j] == target:
                    lst=[i,j]
                    i=len(nums)
                    break
                j=j+1
            i=i+1
        return lst
