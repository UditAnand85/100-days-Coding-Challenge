class Solution:
    def solveSudoku(self, board):
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9
        empty = []

        def bit(d):
            return 1 << (d - 1)

        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    d = int(board[r][c])
                    rows[r] |= bit(d)
                    cols[c] |= bit(d)
                    boxes[(r // 3) * 3 + c // 3] |= bit(d)

        def backtrack(idx):
            if idx == len(empty):
                return True

            r, c = empty[idx]
            b = (r // 3) * 3 + c // 3
            mask = rows[r] | cols[c] | boxes[b]

            for d in range(1, 10):
                if not (mask & bit(d)):
                    board[r][c] = str(d)
                    rows[r] |= bit(d)
                    cols[c] |= bit(d)
                    boxes[b] |= bit(d)

                    if backtrack(idx + 1):
                        return True

                    rows[r] ^= bit(d)
                    cols[c] ^= bit(d)
                    boxes[b] ^= bit(d)
                    board[r][c] = "."

            return False

        backtrack(0)
