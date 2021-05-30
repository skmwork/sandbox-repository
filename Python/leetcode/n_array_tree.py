# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/595/week-3-april-15th-april-21st/3714/
# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
#
# Nary-Tree input serialization is represented in their level order traversal.
# Each group of children is separated by the null value (See examples)
from typing import List


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []

        def dfs(rt):
            res = [rt.val]
            for r in rt.children:
                res.extend(dfs(r))
            return res

        return dfs(root)


root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
s = Solution()
s.preorder(root)
