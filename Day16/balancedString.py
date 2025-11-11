class Solution(object):
    def balancedString(self, s):
        from collections import Counter
        freq = Counter(s)
        n = len(s)
        k = n // 4
        res = n
        left = 0

        for right in range(n):
            freq[s[right]] -= 1 

        
            while left < n and all(freq[c] <= k for c in "QWER"):
                res = min(res, right - left + 1)
                freq[s[left]] += 1  
                left += 1

        return res
