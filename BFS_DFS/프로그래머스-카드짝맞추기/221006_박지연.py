import sys
from collections import deque


def solution(board, r, c):
    answer = 0
    card = 0
    card_list = []
    nr = r
    nc = c

    for i in range(4):
        for j in range(4):
            if board[i][j]!= 0:
                card += 1  # 총 남은 카드의 수
                card_list.append([i,j])

    for i in range(card//2):
        x = nr
        y = nc
        num = board[x][y]
        cnt = 1

        if board[nr][nc] == 0:
            min_num = sys.maxsize
            size = 0
            for j in range(len(card_list)):
                if board[card_list[j][0]][card_list[j][1]] != 0:
                    if x == card_list[j][0] or y == card_list[j][1]:
                        size = 2
                    else:
                        size = 3
                    if min_num > size:
                        min_num = size
                        x = card_list[j][0]
                        y = card_list[j][1]
                        num = board[x][y]
            cnt = min_num

        board[x][y] = 0

        for j in range(len(card_list)):
            if board[card_list[j][0]][card_list[j][1]] == num:
                if x == card_list[j][0] or y == card_list[j][1]:
                    cnt += 2
                    board[card_list[j][0]][card_list[j][1]] = 0
                    nr = card_list[j][0]
                    nc = card_list[j][1]
                    break
                else:
                    cnt += 3
                    board[card_list[j][0]][card_list[j][1]] = 0
                    nr =card_list[j][0]
                    nc = card_list[j][1]
                    break

        answer += cnt


    return answer


'''  
def bfs(r, c, cnt, num, board):
    queue = deque()

    queue.append([r, c, 0, board[r][c]], False, 0, 0)
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y, cnt, num, isCtrl, ctrl_x, ctrl_y = queue.popleft()
        if isCtrl:
            nx = x + ctrl_x
            ny = y + ctrl_y
        else:
            for k in range(4):
                nx = dx[k] + x
                ny = dy[k] + y
                n_cnt = cnt + 1
                
                if 0<= nx < 4 and 0<= ny < 4:
                    if board[nx][ny] == 0:
                        queue.append(nx, ny, n_cnt, 0, True, dx[k], dy[k])
                        queue.append(nx, ny, n_cnt, 0, False)
                    else:
                        
'''





a = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
b = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
print(solution(a, 1, 0))