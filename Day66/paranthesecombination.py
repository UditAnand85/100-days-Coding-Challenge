class Solution:
    def generateParenthesis(self, n):
        res = []

        def backtrack(open_cnt, close_cnt, path):
            if len(path) == 2 * n:
                res.append(path)
                return

            if open_cnt < n:
                backtrack(open_cnt + 1, close_cnt, path + "(")

            if close_cnt < open_cnt:
                backtrack(open_cnt, close_cnt + 1, path + ")")

        backtrack(0, 0, "")
        return res