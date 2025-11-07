class Solution:
    def checkEqual(self, a, b) -> bool:
        freq1 = {}
        freq2 = {}
        for i in a:
            if i in freq1:
                freq1[i] = freq1[i] + 1
            else:
                freq1[i] = 1
        for i in b:
            if i in freq2:
                freq2[i] = freq2[i] + 1
            else:
                freq2[i] = 1
                
        return freq1 == freq2