class Solution(object):
    def sumSubarrayMins(self, arr):
        n = len(arr)
        mod = 10**9 + 7

        prev = [0] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            prev[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

       
        next_ = [0] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            next_[i] = stack[-1] - i if stack else n - i
            stack.append(i)

       
        ans = 0
        for i in range(n):
            ans = (ans + arr[i] * prev[i] * next_[i]) % mod

        return ans
