class Solution(object):
    def arrangeCoins(self, n):
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2   

            if coins == n:
                return mid
            if coins < n:
                left = mid + 1
            else:
                right = mid - 1

        return right  
