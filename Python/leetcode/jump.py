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
