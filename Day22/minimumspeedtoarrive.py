class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        left, right = 1, 10000000
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if self.canArriveOnTime(dist, hour, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return result

    def canArriveOnTime(self, dist, hour, speed):
        time = 0.0
        
     
        for i in range(len(dist) - 1):
            time += (dist[i] + speed - 1) // speed

   
        time += dist[-1] / float(speed)

        return time <= hour
