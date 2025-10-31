class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        longest = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                longest = max(longest, count)
            else:
                count = 0
        return longest