class Solution(object):
    def asteroidCollision(self,asteroids):
        stack = []

        for a in asteroids:
            
            while stack and a < 0 and stack[-1] > 0:
                if abs(stack[-1]) < abs(a):
                    stack.pop() 
                    continue
                elif abs(stack[-1]) == abs(a):
                    stack.pop() 
                break
            else:
                
                stack.append(a)

        return stack

            
            