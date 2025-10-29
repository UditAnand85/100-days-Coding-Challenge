class Solution(object):
    def tribonacci(self, n):
        a = 0
        b = 1
        c = 1
        tribo = 0
        if(n == 0):
            tribo = 0
        elif(n==1):
            tribo= 1 
        elif(n==2):
            tribo =  1
        else:
            for i in range(2,n):
                tribo = a + b + c
                a = b
                b = c
                c = tribo
        return tribo