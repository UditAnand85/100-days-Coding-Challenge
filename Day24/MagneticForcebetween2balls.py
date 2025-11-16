class Solution(object):
    def maxDistance(self, position, m):
        position.sort()
        
        low = 1
        high = position[-1] - position[0]
        ans = 0
        
        while low <= high:
            mid = low + (high - low) // 2 
            
            if self.canPlace(position, m, mid):
                ans = mid
                low = mid + 1        
            else:
                high = mid - 1          
        
        return ans

    def canPlace(self, pos, m, dist):
        count = 1
        last = pos[0]
        
        for i in range(1, len(pos)):
            if pos[i] - last >= dist:
                count += 1
                last = pos[i]
            if count == m:
                return True
        
        return False
