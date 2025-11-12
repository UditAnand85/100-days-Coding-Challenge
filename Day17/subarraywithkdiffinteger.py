from collections import defaultdict

class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        def atMost(k):
            count = 0
            freq = defaultdict(int)
            left = 0

            for right in range(len(nums)):
                freq[nums[right]] += 1

               
                while len(freq) > k:
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        del freq[nums[left]]
                    left += 1

                count += right - left + 1
            return count

        return atMost(k) - atMost(k - 1)
