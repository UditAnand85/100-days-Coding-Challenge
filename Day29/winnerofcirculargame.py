class Solution(object):
    def findTheWinner(self, n, k):
        arr = list(range(1, n + 1))
        idx = 0

        while len(arr) > 1:
            idx = (idx + k - 1) % len(arr)
            arr.pop(idx)                    

        return arr[0]
