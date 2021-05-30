# https://leetcode.com/problems/super-palindromes/
# Let's say a positive integer is a super-palindrome
# if it is a palindrome, and it is also the square of a palindrome.
# Given two positive integers left and right represented as strings,
# return the number of super-palindromes integers in the inclusive range [left, right].
from math import floor, sqrt, ceil


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        cnt = 0
        i = floor(int(left) ** 0.5)
        r = floor(int(right) ** 0.5)
        while i <= r:
            dq = i ** 2
            sdq = str(dq)
            f = str(i)
            if sdq == sdq[::-1] and f == f[::-1]:
                cnt += 1
            l = len(f)
            if l == 1:
                i = int(i) + 1
                continue
            c = ceil(len(f) / 2)
            z = f[:c]
            f = str(int(z) + 1) if f[0] <= f[l - 1] else z
            c2 = len(f)
            if c < c2 and c2 % 2 == 1 or c < c2 and c2 % 2 == 0 and l % 2 == 0:
                c2 = c2 - 1
            if c < c2 and c2 % 2 == 0 and l % 2 == 1:
                f = f[:c2 - 1]
            if l % 2 == 1:
                c2 = c2 - 1
            i = int(f + f[:c2][::-1])
        return cnt


s = Solution()
print(s.superpalindromesInRange("1", "232747148"))
