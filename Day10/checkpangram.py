class Solution(object):
    def checkIfPangram(self, sentence):
        s = "abcdefghijklmnopqrstuvwxyz"
        for i in s:
            if i not in sentence:
                return False
        return True
        