class Solution(object):
    def rowAndMaximumOnes(self, mat):
        max1 = 0
        answer = 0
        for i in range(0,len(mat)):
            total1 = 0
            for j in range(0,len(mat[0])):
                if mat[i][j] == 1:
                    total1 = total1 + 1

            if max1 < total1:
                max1 = total1
                answer = i
            
        return [answer,max1]
