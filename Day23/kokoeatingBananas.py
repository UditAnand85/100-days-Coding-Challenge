class Solution(object):
    def minEatingSpeed(self, piles, h):
        low = 1
        high = 0

        for pile in piles:
            high = max(high, pile); 
        while (low < high):
            mid = low + (high - low) / 2
            if self.canFinish(piles, mid, h):
                high = mid
            else :
                low = mid + 1
        
        
        return low; 
    
    def canFinish(self,piles, k, h):
        time = 0
        for pile in piles:
            time += (pile + k - 1) / k
        
        return time <= h
        