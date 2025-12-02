class Solution(object):
    def subsets(self, nums):
        res = [[]]
    
        for x in nums:
            new_sets = []
            for s in res:
                new_sets.append(s + [x])
            res += new_sets
        
        return res
        