class Solution:
    def countSetBits(self, n):
        ans = 0
        x = 0
        
        while (1 << x) <= n:
            full_cycles = (n + 1) // (1 << (x + 1))
            ans += full_cycles * (1 << x)
            
            leftover = (n + 1) % (1 << (x + 1))
            ans += max(0, leftover - (1 << x))
            
            x += 1
        
        return ans
