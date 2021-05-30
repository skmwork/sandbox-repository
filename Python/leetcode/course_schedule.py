# https://leetcode.com/explore/featured/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3729/
# There are n different online courses numbered from 1 to n.
# You are given an array courses where courses[i] = [duration i, lastDay i]
# indicate that the ith course should be taken continuously for duration i days and must be finished
# before or on lastDay i.

from typing import List
import heapq
from operator import itemgetter


class Solution:

    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=itemgetter(1))
        w, h = 0, []
        for c in courses:
            r = w + c[0]
            if r <= c[1]:
                w = r
                heapq.heappush(h, -c[0])
            else:
                if h and -h[0] > c[0] and c[0]:
                    w = w - (-heapq.heappop(h)) + c[0]
                    heapq.heappush(h, -c[0])
        return len(h)


s = Solution()
print(s.scheduleCourse([[7, 17], [3, 12], [10, 20], [9, 10], [5, 20], [10, 19], [4, 18]]))
