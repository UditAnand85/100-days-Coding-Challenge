class Solution1(object):
    def addBinary(self, a, b):
        return bin(int(a,2)+int(b,2))[2:]
    
class Solution2(object):
    def addBinary(self, a, b):
        a = self.binarytodecimal(a)
        b = self.binarytodecimal(b)
        return self.decimaltobinary(str(a+b))

    def binarytodecimal(self,b):
        size = len(b)
        number = 0
        for i in range(size):
            number = number + int(b[i])*(2**(size-(i+1)))
        return number
    
    def decimaltobinary(self,b):
        b = int(b)
        if b == 0:
            return "0"
        binary = ""
        while b > 0:
            binary += str(b % 2)
            b //= 2
        return binary[::-1]


