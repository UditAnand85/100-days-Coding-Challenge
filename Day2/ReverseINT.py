class Solution(object):
    def reverse(self, x):
        reverse = 0
        if (x > 0):
            for i in range(0,len(str(x))):
                reverse = (reverse * 10) + x % 10
                x = x // 10
        else:
            x = x - (x * 2) 
            for i in range(0,len(str(x))):
                reverse = (reverse * 10) + x % 10
                x = x // 10
            reverse = 0 - reverse
        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0
        return reverse
    
sol = Solution()
print(sol.reverse(432))