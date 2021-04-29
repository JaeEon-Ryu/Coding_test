'''
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
'''


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]

        # left to right
        for i in range(len(ratings) - 1):
            if ratings[i] < ratings[i + 1]:
                candies.append(candies[-1] + 1)
            else:
                candies.append(1)

        # right to left
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
