class Solution(object):
    def findDuplicate(self, nums):
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i] = dict1[i] + 1
            else:
                dict1[i] = 1
                
            if dict1[i] > 1:
                return i
        