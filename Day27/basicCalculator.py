class Solution(object):
    def calculate(self, s):
        stack = []
        curr = 0
        sign = 1
        result = 0

        for ch in s:
            if ch.isdigit():
                curr = curr * 10 + int(ch)

            elif ch == '+':
                result += sign * curr
                curr = 0
                sign = 1

            elif ch == '-':
                result += sign * curr
                curr = 0
                sign = -1

            elif ch == '(':
           
                stack.append(result)
                stack.append(sign)

        
                result = 0
                sign = 1

            elif ch == ')':
                result += sign * curr
                curr = 0

                
                sign = stack.pop()
                prev_result = stack.pop()

                result = prev_result + sign * result

        return result + sign * curr
