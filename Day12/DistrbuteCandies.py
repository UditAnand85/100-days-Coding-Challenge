class Solution(object):
    def distributeCandies(self, candyType):
        candy = set(candyType)
        if len(candy) > len(candyType)/2:
            return len(candyType)/2
        else:
            return len(candy)
        