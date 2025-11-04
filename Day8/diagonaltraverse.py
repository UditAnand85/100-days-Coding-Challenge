class Solution(object):
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []
        
        rows, cols = len(matrix), len(matrix[0])
        result = []
        r = c = 0
        direction = 1 
        
        for _ in range(rows * cols):
            result.append(matrix[r][c])
            
            if direction == 1:
                if c == cols - 1: 
                    r += 1
                    direction = -1
                elif r == 0:       
                    c += 1
                    direction = -1
                else:
                    r -= 1
                    c += 1
            else:
                if r == rows - 1: 
                    c += 1
                    direction = 1
                elif c == 0:       
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1
        
        return result
