class Solution:
    def firstElementKTime(self, arr,k):
        freq_dict = {}
        for i in arr:
            if i in freq_dict:
                freq_dict[i] = freq_dict[i] + 1
            else:
                freq_dict[i] = 1
            
            if freq_dict[i] == k:
                return i
        return -1
