class Solution:
    def josephus(self, n, k):
        ans = 0
        for i in range(1, n + 1):
            ans = (ans + k) % i
        return ans + 1
