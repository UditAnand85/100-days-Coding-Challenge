class Solution:
    def countBits(self, n):
        ans = []
        for i in range(n + 1):
            cnt = 0
            x = i
            while x > 0:
                cnt += (x & 1)
                x = x >> 1
            ans.append(cnt)
        return ans
