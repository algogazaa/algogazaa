import copy
from collections import deque

def solution(n, blocks):
    answer = 0
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for x, y in blocks:
        visited[x-1][y-1] = -1

    qq = deque()
    qq.append([visited, 0])
    for i in range(n):
        for j in range(n):
            if visited[i][j] != -1:
                copy_q = deque()
                while qq:
                    is_visited, count = qq.popleft()
                    copy_q.append([is_visited, count])

                    if is_visited[i][j] == 0:
                        copy_vis = copy.deepcopy(is_visited)
                        isOk, return_vis = isRK(i, j, copy_vis, n)

                        if isOk:
                            if count + 1 == n:
                                answer += 1
                            else:
                                copy_q.append([return_vis, count + 1])
                qq = copy_q

    return answer

def isRK(x, y, visited, n):
    dx = [1, 1, 2, 2, -1, -1, -2, -2, 1, -1, 0, 0]
    dy = [-2, 2, 1, -1, 2, -2, 1, -1, 0, 0, 1, -1]
    isOk = True
    queue = deque()
    visited[x][y] = -2
    for i in range(12):
        queue.append([x, y, i])

    while queue:
        a, b, i = queue.popleft()
        nx = a + dx[i]
        ny = b + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == 0:
                visited[nx][ny] = -3
                queue.append([nx, ny, i])
            elif visited[nx][ny] == -2:
                isOk = False
                break
            elif visited[nx][ny] == -1:
                queue.append([nx, ny, i])

    return isOk, visited


print(solution(3, [[1, 2], [2, 1]]))
print(solution(4, [[1, 3], [1, 4], [2, 1], [2, 2], [3, 3], [3, 4], [4, 1], [4, 2]]))
print(solution(2, [[1, 1]]))