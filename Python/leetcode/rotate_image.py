# https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3720/
#
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).


class Solution:
    def rotate(self, matrix):
        x = len(matrix[0])-1
        for r in range(x//2+1):
            for c in range(x-r*2):
                rc ,xr= r+c,x - r
                xrc=xr-c
                matrix[r][rc],matrix[rc][xr] = matrix[rc][xr],matrix[r][rc]
                matrix[xr][xrc], matrix[xrc][r] = matrix[xrc][r],matrix[xr][xrc]
                matrix[r][rc] , matrix[xr][xrc] = matrix[xr][xrc],matrix[r][rc]

solution = Solution()
m = [[1,2,3],[4,5,6],[7,8,9]]
print(m)
solution.rotate(m)
print(m)