class Solution(object):
    def intersection(self, nums1, nums2):
        n1 = set(nums1)
        n2 = set(nums2)
        result = []
        for i in n1:
            if i in n2:
                result.append(i)
        
        return result
        