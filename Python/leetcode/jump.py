# https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3732/
# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# You can assume that you can always reach the last index.

class Solution:
    def jump(self, nums):
        res, ln = [0 for _ in nums], len(nums)
        if len(nums) == 1 and nums[0] > 0:
            return 0
        for i in range(ln):
            em, ri = nums[i], res[i]
            if i + 1 < ln and (res[i + 1] > ri + 1 or res[i + 1] == 0):
                res[i + 1] = ri + 1
            if em > 0 and i + em < ln and (res[i + em] > ri + 1 or res[i + em] == 0):
                for j in range(i + 1, i + em + 1):
                    if res[j] > ri + 1 or res[j] == 0:
                        res[j] = ri + 1
            if em > 0 and i + em >= len(nums) and i + 1 != ln and (
                    res[ln - 1] > ri + 1 or res[ln - 1] == 0):
                res[ln - 1] = ri + 1
        return (res[-1])


s = Solution()
print(s.jump([4, 1, 1, 3, 1, 1, 1]))
