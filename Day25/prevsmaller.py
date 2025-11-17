class Solution:
	def prevSmaller(self,arr):
        stack = []
        res = []
    
        for num in arr:
            while stack and stack[-1] >= num:
                stack.pop()
    
            res.append(stack[-1] if stack else -1)
    
            stack.append(num)
    
        return res

		