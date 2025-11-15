class Solution(object):
    def smallestDivisor(self, nums, threshold):
        left, right = 1, max(nums)

        def compute(div):
            total = 0
            for x in nums:
                total += (x + div - 1) // div 
            return total

        while left < right:
            mid = (left + right) // 2

            if compute(mid) <= threshold:
                right = mid
            else:
                left = mid + 1

        return left
