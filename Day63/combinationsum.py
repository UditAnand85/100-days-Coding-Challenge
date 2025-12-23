class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])  
                path.pop()

        backtrack(0, [], target)
        return res
        