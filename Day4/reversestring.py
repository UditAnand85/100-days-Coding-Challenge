class Solution(object):
    def reverseString(self, s):
        if(len(s)==1):
            return s
        else:
            for i in range(0,len(s)//2):
                temp = s[i]
                s[i] = s[len(s)-(1+i)]
                s[len(s)-(1+i)] = temp
        return s