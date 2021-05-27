from typing import List

root = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]


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


s = Solution()
s.preorder(root)
