class Solution(object):
    def numTrees(self, n):
        value = self.fac(n*2) / (self.fac(n) * self.fac(n))
        return value / (n + 1)


    def fac(self,n):
        if(n == 1):
            return 1
        else:
            return n * self.fac(n-1)
        