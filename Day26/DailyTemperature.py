class Solution(object):
    def dailyTemperatures(self,temperatures):
        n = len(temperatures)
        result = [0] * n
        stack = []  

        for i, current in enumerate(temperatures):
            while stack and current > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)

        return result
   
        