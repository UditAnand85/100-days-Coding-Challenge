class Solution(object):
    def totalFruit(self, fruits):
        counts = {}
        left = 0
        max_len = 0

        for right, f in enumerate(fruits):
            counts[f] = counts.get(f, 0) + 1

            while len(counts) > 2:
                counts[fruits[left]] -= 1
                if counts[fruits[left]] == 0:
                    del counts[fruits[left]]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
