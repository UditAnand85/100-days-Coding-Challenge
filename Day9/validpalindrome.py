class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        newS = ""
        for i in s:
            if i.isalnum():
                newS += i
        return newS == newS[::-1]
