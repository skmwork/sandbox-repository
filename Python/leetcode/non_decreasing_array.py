# https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3731/
# Given an array nums with n integers, your task is to check
# if it could become non-decreasing by modifying at most one element.


from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        ln = len(nums)
        if not nums:
            return False
        if len(nums) == 1:
            return True
        prev = None
        for i in range(ln-1):
            if nums[i] > nums[i+1]:
                if prev is not None:
                    return False
                prev = i
        if prev is not None:
            if prev+2 == ln:
                return True
            if prev == 0:
                return True
            if nums[prev+1] >= nums[prev-1]:
                return True
            if nums[prev] <= nums[prev+2]:
                return True
            return False
        return True


s = Solution()
#print(s.checkPossibility([4, 2, 3]))
print(s.checkPossibility([1,3,4,2,5]))
#print(s.checkPossibility([4,2,1]))