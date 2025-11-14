class Solution(object):

    def search(self, nums, target):
        left = 0
        right = len(nums)-1
       
        while(left<=right):
            center = left + (right - left)// 2
            if target == nums[center]:
                return center
            elif target > nums[center]:
                left = center + 1
            else:
                right = center - 1
                
        return -1

        