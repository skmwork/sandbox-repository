# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/596/week-4-april-22nd-april-28th/3719/
# Critical Connections in a Network
# A critical connection is a connection that, if removed, will make some server unable to reach some other server.
# 4 [[1,0],[2,0],[3,0],[4,1],[4,2],[4,0]] -> [[3, 0]]

class Solution:
    def criticalConnections(self, n: int, connections):
        if not connections or not connections[0] or connections[0][0] is None:
            return []
        G = {}
        def set_edge(k, v):
            gv = G.get(k, [])
            gv.append(v)
            G[k] = gv
        for e in connections:
            set_edge(e[0], e[1])
            set_edge(e[1], e[0])
        h, d, used = [0] * n, [0] * n, [False] * n
        criticals = []
        def dfs(v, p=-1):
            used[v] = True
            d[v] = h[v] = (0 if p == -1 else h[p] + 1)
            for u in G.get(v, []):
                if u != p:
                    if used[u]:
                        d[v] = min(d[v], h[u])
                    else:
                        dfs(u, v)
                        d[v] = min(d[v], d[u])
                        if h[v] < d[u]:
                            criticals.append([u, v])
        dfs(next(iter(G)))
        return criticals


solution = Solution()
print(solution.criticalConnections(5, [[1,0],[2,0],[3,0],[4,1],[4,2],[4,0]]))