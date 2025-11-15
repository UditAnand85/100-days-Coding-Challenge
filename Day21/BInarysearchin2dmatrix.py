class Solution(object):
    def searchMatrix(self, matrix, target):
        left = 0
        row = 0
        right = len(matrix[row])-1
        
        
        while(left<=right):
            center = (left + right)//2
            if matrix[row][right] < target:
                row  += 1
                if row == len(matrix):
                    return False
                continue

            if target == matrix[row][center]:
                return True
            elif target > matrix[row][center]:
                left = center + 1
            else:
                right = center - 1
                
        return False