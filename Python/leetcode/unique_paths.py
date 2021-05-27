#https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3723/


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        x, y = len(obstacleGrid[0])-1, len(obstacleGrid)-1
        for i in range(y+1):
            for j in range(x+1):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        def move(i,j):
            if i > y or j > x or obstacleGrid[i][j] == -1:
                return 0
            if i == y and j == x and obstacleGrid[i][j]==0:
                obstacleGrid[i][j] = 1
                return 1
            if obstacleGrid[i][j]!= -1 and (obstacleGrid[i][j]>0 ):
                return obstacleGrid[i][j]
            if i <= y:
                obstacleGrid[i][j]+=move(i + 1, j)
            if j<=x:
                obstacleGrid[i][j]+=move(i, j + 1)
            return obstacleGrid[i][j]
        move(0, 0)
        return obstacleGrid[0][0] if obstacleGrid[0][0]> 0 else 0