class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        index_dict = {}
        
        for i, num in enumerate(nums):
            if num in index_dict and i - index_dict[num] <= k:
                return True
            index_dict[num] = i
        
        return False

        