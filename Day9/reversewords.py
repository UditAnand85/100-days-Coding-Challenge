class Solution(object):
    def reverseWords(self, s):
        ls = s.split()
        ls = ls[::-1]

        s = " ".join(ls)
        return s
        