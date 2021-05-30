# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3715/
# Given a triangle array, return the minimum path sum from top to bottom.
#
# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row,
# you may move to either index i or index i + 1 on the next row.
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for l in range(len(triangle)-1,0,-1):
            for j in range(l):
                triangle[l-1][j]=triangle[l-1][j]+min(triangle[l][j],triangle[l][j+1])
        return triangle[0][0]

s = Solution()
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

print(s.minimumTotal(triangle))