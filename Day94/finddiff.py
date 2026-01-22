class Solution(object):
    def findTheDifference(self, s, t):
        sumt = 0
        for i in t:
            sumt = sumt + ord(i)

        sums = 0
        for j in s:
            sums = sums + ord(j)
        return chr(sumt-sums)
