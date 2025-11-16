class Solution(object):
    def shipWithinDays(self, weights, days):
        low = max(weights)
        high = sum(weights)
        
        while low < high:
            mid = low + (high - low) // 2
            
            if self.canShip(weights, mid, days):
                high = mid
            else:
                low = mid + 1
        
        return low

    def canShip(self, weights, capacity, days):
        curr_sum = 0
        needed_days = 1
        
        for w in weights:
            if curr_sum + w > capacity:
                needed_days += 1
                curr_sum = w
            else:
                curr_sum += w
        
        return needed_days <= days
