# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3718/
# Give a string s, count the number of non-empty (contiguous)
# substrings that have the same number of 0's and 1's, and
# all the 0's and all the 1's in these substrings are grouped consecutivel
# Substrings that occur multiple times are counted the number of times they occur.
# "10101" -> 4
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt, prev_sub, sub = 0, 0, 0
        for curr in range(len(s)):
            if not curr or s[sub] != s[curr]:
                prev_sub = sub
                sub = curr
            if prev_sub < sub:
                prev_sub += 1
                cnt += 1
        return cnt


solution = Solution()
print(solution.countBinarySubstrings("001110011"))