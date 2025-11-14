class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)-1
       
        while left <= right:
            center = left + (right - left)//2
            
            if nums[center] == target:
                return center
            elif nums[center] < target:
                left = center + 1
            else:
                right = center - 1
        
        return left
