class Solution(object):
    def intersect(self, nums1, nums2):
        freq = {}
        for i in nums1:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        result = []
        
        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        
        return result
