# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3703/
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
#
# From each cell, you can either move in four directions: left, right, up, or down. You may not move
# diagonally or move outside the boundary (i.e., wrap-around is not allowed).
from itertools import product


class Solution:
    def longestIncreasingPath(self, matrix):
        def get_edges():
            n_range, m_range, matrix_len_range = range(n), range(m), range(matrix_len)
            stems, graph = [0 for x in matrix_len_range], [[] for x in matrix_len_range]
            for row_num, col_num in product(m_range, n_range):
                num = n * row_num + col_num
                value = matrix[row_num][col_num]
                if row_num > 0:
                    set_path(stems, graph, num, value, num - n, matrix[row_num - 1][col_num])
                if col_num > 0:
                    set_path(stems, graph, num, value, num - 1, matrix[row_num][col_num - 1])
            for g in graph:
                g.sort(reverse=True)
            leaves = sorted([i for i, k in enumerate(stems) if not k])
            return leaves, graph

        def set_path(stems, graph, num, value, prev_num, prev_value):
            if value > prev_value:
                graph[prev_num].append(num)
                if not stems[num]:
                    stems[num] = 1
            if value < prev_value:
                if not stems[prev_num]:
                    stems[prev_num] = 1
                graph[num].append(prev_num)

        def max_path(leaves, graph):
            max_paths_len = [0] * len(graph)
            for k in leaves:
                v = [(k, 1)]
                while v:
                    e, current_level = v.pop()
                    if max_paths_len[e] >= current_level:
                        continue
                    max_paths_len[e] = current_level
                    current_level += 1
                    for g in graph[e]:
                        if max_paths_len[g] < current_level:
                            v.append((g, current_level))
            return max(max_paths_len)

        n, m = len(matrix[0]), len(matrix)
        matrix_len = m * n
        return max_path(*get_edges())


matrix = [[9, 9, 4], [6, 6, 8], [2, 1, 1]]
s = Solution()
print(s.longestIncreasingPath(matrix))
