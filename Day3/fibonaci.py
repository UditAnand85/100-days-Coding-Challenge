class Solution(object):
    def fib(self, n):
        a = 0
        b = 1
        fibo = 0
        if(n==0):
            fibo = 0
        elif(n==1):
            fibo = 1
        else:
            for i in range(1,n):
                fibo = a + b
                a = b
                b = fibo
        return fibo
        
sol = Solution()
print(sol.fib(5))