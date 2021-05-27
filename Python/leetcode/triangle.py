from typing import List

triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for l in range(len(triangle)-1,0,-1):
            for j in range(l):
                triangle[l-1][j]=triangle[l-1][j]+min(triangle[l][j],triangle[l][j+1])
        return triangle[0][0]
s = Solution()
print(s.minimumTotal(triangle))