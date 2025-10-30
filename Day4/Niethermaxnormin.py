class Solution(object):
    def findNonMinOrMax(self, nums):
        if len(nums) < 3:
            return -1
        else:
            Max = nums[0]
            Min = nums[0]
            for i in range(0,len(nums)):
                if(nums[i]>Max):
                    Max = nums[i]
                if(nums[i]<Min):
                    Min = nums[i]
            for i in range(0,len(nums)):
                if(nums[i] != Max and nums[i] != Min):
                    return nums[i]