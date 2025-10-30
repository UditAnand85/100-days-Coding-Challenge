class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        sum_arr = 0
        for i in range(0,n):
            sum_arr = sum_arr + nums[i]
        return expected_sum - sum_arr
