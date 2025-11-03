class Solution(object):
    def diagonalSum(self, mat):
        sum = 0
        for i in range(0,len(mat)):
            for j in range(0,len(mat[i])):
                if i == j:
                    sum = sum + mat[i][j]
            sum = sum + mat[i][(len(mat)-1)-i]

        if len(mat) % 2 == 1:                        
            sum = sum - mat[len(mat) // 2][len(mat) // 2]
        return sum