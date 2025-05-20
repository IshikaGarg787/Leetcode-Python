# wap to return number of unique elements in nums
class Solution:
    def removeDuplicates(self, nums):
        k = 1
        for i in range(1,len(nums)):   
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k+=1
        return k 
