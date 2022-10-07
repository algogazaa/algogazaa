from collections import deque


def solution(maps):
    n = len(maps)  #x좌표
    m = len(maps[0])  #y좌표
    answer = -1

    isvisited = [[False for _ in range(m)]for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append([0, 0, 1])
    isvisited[0][0] = True
    while queue:
        x, y, cnt = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            n_cnt = cnt + 1

            if 0<= nx < n and 0<= ny < m and isvisited[nx][ny] == False:
                if maps[nx][ny] == 1:
                    if nx == n-1 and ny == m-1:
                        if answer == -1:
                            answer = n_cnt
                        else:
                            answer = min(answer, n_cnt)
                    else:
                        isvisited[nx][ny] = True
                        queue.append([nx, ny, n_cnt])

    return answer

a = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
b = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]

print(solution(b))