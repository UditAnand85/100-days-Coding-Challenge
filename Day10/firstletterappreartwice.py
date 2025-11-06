class Solution(object):
    def repeatedCharacter(self, s):
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
            if freq[char] == 2:
                return char