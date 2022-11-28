#
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
q = list(map(int, input().split()))
k = list(map(int, input().split()))
p = list(map(int, input().split()))
board = [['0'] * m for _ in range(n)]

for i in range(1,len(q),2):
    board[q[i] - 1][q[i + 1] - 1] = 'q'

for i in range(1, len(k), 2):
    board[k[i] - 1][k[i + 1] - 1] = 'k'

for i in range(1, len(p), 2):
    board[p[i] - 1][p[i + 1] - 1] = 'p'

def dfsQ(x,y):
    dx = [0,0,1,-1,1,-1,1,-1]
    dy = [1,-1,0,0,1,1,-1,-1]

    
    for i in range(8):
        nx,ny = x,y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'p' and board[nx][ny] != 'k' and board[nx][ny] != 'q':
                board[nx][ny] = '1'
                continue
            else:
                break
    return

def dfsK(x, y):
    dx = [-1,1,-2,2,-2,2,-1,1]
    dy = [-2,-2,-1,-1,1,1,2,2]

    
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 'p' and board[nx][ny] != 'k' and board[nx][ny] != 'q':
            board[nx][ny] = '1'
    
    return

for i in range(1,len(q),2):
    dfsQ(q[i] - 1, q[i + 1] - 1)

for i in range(1, len(k), 2):
    dfsK(k[i] - 1, k[i + 1] - 1)
    
result = 0
for b in board:
    result += b.count("0")
print(result)