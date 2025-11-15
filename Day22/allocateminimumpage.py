class Solution:
    def findPages(self, arr, k):

        n = len(arr)
      
        if k > n:
            return -1

        left = max(arr)      
        right = sum(arr)     


        def canAllocate(limit):
            students = 1
            pages = 0

            for x in arr:
                if pages + x <= limit:
                    pages += x
                else:
                    students += 1
                    pages = x
            return students <= k

        while left < right:
            mid = (left + right) // 2

            if canAllocate(mid):
                right = mid
            else:
                left = mid + 1

        return left
