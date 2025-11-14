class Solution(object):
    def findPeakElement(self, nums):
        max1 = float("-inf")
        max2 = 0
        for i in range(0,len(nums)):
            if nums[i] > max1 :
                max1 = nums[i]
                max2 = i
        return max2
        