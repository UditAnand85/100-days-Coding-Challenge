class Solution:
    def RopeCutting(self, arr):
        arr.sort()
        res = []
        n = len(arr)
        i = 0

        while i < n:
            curr = arr[i]
            while i < n and arr[i] == curr:
                i += 1
            if i < n:
                res.append(n - i)

        return res
