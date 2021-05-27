

import heapq
#https://leetcode.com/explore/featured/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3721/
#You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.


class Solution:
    def furthestBuilding(self, heights, bricks, ladders):
        b, prev , curr ,i , ldr = bricks, 0, heights[0], 1,[]
        heapq.heapify(ldr)
        while i < len(heights):
            prev = curr
            curr = heights[i]
            if prev >= curr:
                i += 1
                continue
            diff = curr - prev
            if diff == 1 and b:
                b -= 1
                i+=1
                continue
            if not ldr or (len(ldr) < ladders and ldr[0]>0):
                heapq.heappush(ldr, 0)

            if ldr:
                ld = ldr[0]
                if ladders > 0 and (diff > 1 or not b) and diff > ld:
                    heapq.heappushpop(ldr, diff)
                    diff = ld
            if b >= diff:
                b -= diff
            else:
                break
            i += 1
        return i - 1