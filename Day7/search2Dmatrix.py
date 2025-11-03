class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                if matrix[i][j] == target:
                    return True

        return False
         
        