class Solution(object):
    def splitArray(self, nums, m):

        left = max(nums)       
        right = sum(nums)       

        def canSplit(maxSum):
            count = 1
            current = 0

            for x in nums:
                if current + x <= maxSum:
                    current += x
                else:
                    count += 1
                    current = x
            return count <= m

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left
