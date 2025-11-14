class Solution(object):
    def isPerfectSquare(self, num):
        left = 0
        right = num
        while(left <= right ):
            mid = left + (right - left)//2 
            sqr = mid * mid
            if sqr == num:
                return True
            elif sqr > num:
                right = mid-1
            else:
                left = mid + 1
            
        return False