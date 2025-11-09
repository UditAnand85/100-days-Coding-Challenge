class Solution:
    def firstNegInt(self, arr, k): 
        a = 0
        b = k
        result = []
        for i in range(0,len(arr)-k+1):
            for j in range(a,b):
                num = 0
                if arr[j]<0:
                    num = arr[j]
            result.append(num)
            
            a = a+1
            b = b+1
                 
        return result