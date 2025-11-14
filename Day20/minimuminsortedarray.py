class Solution(object):
    def findMin(self, nums):
        min1 = float("inf")
        for i in nums:
            if i < min1:
                min1 = i
        return min1 
        