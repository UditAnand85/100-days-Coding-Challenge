class Solution(object):
    def aggressiveCows(self, stalls, cows):
        stalls.sort()
        low = 1
        high = stalls[-1] - stalls[0]
        ans = 0
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if self.canPlace(stalls, cows, mid):
                ans = mid
                low = mid + 1   
            else:
                high = mid - 1  
        
        return ans
    
    def canPlace(self, stalls, cows, dist):
        count = 1
        last_pos = stalls[0]
        
        for i in range(1, len(stalls)):
            if stalls[i] - last_pos >= dist:
                count += 1
                last_pos = stalls[i]
            if count == cows:
                return True
        
        return False
