class Solution(object):
    def isPalindrome(self, x):
        if(x<0):
            return False
        else:
            orignal = x
            rev = 0
            for i in range(0,len(str(x))):
                rev = (rev*10) + x % 10
                x = x // 10
            return rev == orignal
            