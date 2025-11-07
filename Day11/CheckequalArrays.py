class Solution(object):
    def containsDuplicate(self, nums):
        freq1 = {}
        for i in nums:
            if i in freq1:
                freq1[i] += 1
            else:
                freq1[i] = 1
            
            if freq1[i] > 1:
                return True
        return False
            
        