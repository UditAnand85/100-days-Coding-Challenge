class Solution:
    def maximumTastiness(self, price, k):
        price.sort()
        
        low = 0
        high = price[-1] - price[0]
        ans = 0
        
        def canPick(dist):
            count = 1
            last = price[0]
            
            for i in range(1, len(price)):
                if price[i] - last >= dist:
                    count += 1
                    last = price[i]
                    if count == k:
                        return True
            return False
        
        while low <= high:
            mid = (low + high) // 2
            if canPick(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
