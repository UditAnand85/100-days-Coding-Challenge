class Solution(object):
    def minDays(self, bloomDay, m, k):
        if m * k > len(bloomDay):
            return -1
        
        low = min(bloomDay)
        high = max(bloomDay)
        
        while low < high:
            mid = low + (high - low) // 2
            
            if self.canMake(bloomDay, m, k, mid):
                high = mid
            else:
                low = mid + 1
        
        return low

    def canMake(self, bloomDay, m, k, day):
        bouquets = 0
        flowers = 0
        
        for bloom in bloomDay:
            if bloom <= day:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
            
            if bouquets >= m:
                return True
        
        return False
