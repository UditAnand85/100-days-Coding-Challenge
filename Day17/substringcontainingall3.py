class Solution(object):
    def numberOfSubstrings(self, s):
        from collections import defaultdict
        
        freq = defaultdict(int)
        left = 0
        count = 0
        
        for right in range(len(s)):
            freq[s[right]] += 1
      
            while all(freq[c] > 0 for c in "abc"):

                count += len(s) - right
                
                freq[s[left]] -= 1
                left += 1
        
        return count
