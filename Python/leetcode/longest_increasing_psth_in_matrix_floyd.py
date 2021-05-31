# https://leetcode.com/explore/challenge/card/april-leetcoding-challenge-2021/594/week-2-april-8th-april-14th/3703/
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.
#
# From each cell, you can either move in four directions: left, right, up, or down. You may not move
# diagonally or move outside the boundary (i.e., wrap-around is not allowed).

from itertools import product

inf = 99


def set_path(matrix, graph, row_num, col_num, prev_row_num, prev_col_num):
    num = len(matrix[0]) * row_num + col_num
    prev_num = len(matrix[0]) * prev_row_num + prev_col_num
    prev_value = matrix[prev_row_num][prev_col_num]
    value = matrix[row_num][col_num]
    if value - prev_value > 0:
        graph.append([prev_num + 1, num + 1, 1])
    if value - prev_value < 0:
        graph.append([num + 1, prev_num + 1, 1])


def create_graph(matrix):
    graph = []
    for row_num in range(len(matrix)):
        for col_num in range(len(matrix[row_num])):
            if row_num - 1 >= 0:
                set_path(matrix, graph, row_num, col_num, row_num - 1, col_num)
            if col_num - 1 >= 0:
                set_path(matrix, graph, row_num, col_num, row_num, col_num - 1)
    return graph


def floyd_warshall(n, edge):
    dist = [[inf] * n for i in range(n)]
    nxt = [[0] * n for i in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for u, v, w in edge:
        dist[u - 1][v - 1] = w
        nxt[u - 1][v - 1] = v - 1

    for k, i, j in product(range(n), repeat=3):
        sum_ik_kj = dist[i][k] + dist[k][j]
        if dist[i][k] != inf and dist[k][j] != inf and (dist[i][j] < sum_ik_kj or dist[i][j] == inf):
            dist[i][j] = sum_ik_kj
            nxt[i][j] = nxt[i][k]
    return dist, nxt


def restore_paths(n, dist, nxt):
    paths = []
    for i, j in product(range(n), repeat=2):
        if i != j and dist[i][j] != inf:
            path = [i]
            while path[-1] != j:
                path.append(nxt[path[-1]][j])
            paths.append([dist[i][j], path])
    return paths


def max_restored_path(paths):
    return sorted(paths, reverse=True)[0][1] if len(paths) >= 1 else []


def restore_paths(n, dist, nxt):
    paths = []
    for i, j in product(range(n), repeat=2):
        if i != j and dist[i][j] != inf:
            path = [i]
            while path[-1] != j:
                path.append(nxt[path[-1]][j])
            paths.append([dist[i][j], path])
    return paths


def matrix_path(matrix, path):
    mp = []
    for p in path:
        rn = p // len(matrix[0])
        cn = p % len(matrix[0])
        mp.append(matrix[rn][cn])
    return mp


def max_path(matrix):

    ml = list(map(len, matrix))
    max_len = min(ml)
    min_len = max(ml)
    if min_len != max_len:
        raise AttributeError('max_len != min_len')
    n = max_len
    m = len(matrix)
    matrix_len = m * n

    graph = create_graph(matrix)
    dist, nxt = floyd_warshall(matrix_len, graph)
    paths = restore_paths(matrix_len, dist, nxt)
    max_rest_path = max_restored_path(paths)
    path = matrix_path(matrix, max_rest_path)
    output = f"Input: matrix = {matrix}\r\nOutput: {len(path)}"
    output += f"\r\nExplanation: The longest path is "f"{path}" if path else ""
    print(output)


if __name__ == '__main__':
    max_path([[3, 4, 5], [4, 5, 6], [3, 2, 1]])
    max_path([[9, 9, 4], [6, 6, 8], [2, 2, 1]])
    max_path([[1]])
    max_path([[1, 2, 3], [6, 5, 4], [7, 8, 9]])
    max_path([[7, 10, 12], [6, 5, 4], [1, 2, 3]])
    max_path([[7, 10, 12, 10], [6, 5, 4, 13]])
    max_path([[7, 10, 12], [6, 5, 4]])
    max_path([[7], [6]])


