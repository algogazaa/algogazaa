n, m = map(int, input().split())
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))
board = [['0' for _ in range(m)] for _ in range(n)]
cnt = 0

for a in range(1, queen[0] * 2, 2):
    board[queen[a] - 1][queen[a + 1] - 1] = 'q'

for a in range(1, knight[0] * 2, 2):
    board[knight[a] - 1][knight[a + 1] - 1] = 'k'

for a in range(1, pawn[0] * 2, 2):
    board[pawn[a] - 1][pawn[a + 1] - 1] = 'p'

# Queen 확인_dfs
def check_q(x, y):
    qx = [-1,0,1,1,1,0,-1,-1]
    qy = [-1,-1,-1,0,1,1,1,0]
    for a in range(8):
        temp_x = x
        temp_y = y
        while True:
            temp_x, temp_y = temp_x+qx[a], temp_y+qy[a]
            if 0 <= temp_x < n and 0 <= temp_y < m:
                if board[temp_x][temp_y] == '0':
                    board[temp_x][temp_y] = '1'
                elif board[temp_x][temp_y] == 'k':
                    break
                elif board[temp_x][temp_y] == 'p':
                    break
            else:
                break

# Knight 확인
def check_k(x, y):
    kx = [-2,-1,1,2,2,1,-1,-2]
    ky = [-1,-2,-2,-1,1,2,2,1]
    for a in range(8):
        temp_x, temp_y = x+kx[a], y+ky[a]
        if 0 <= temp_x < n and 0 <= temp_y < m:
            if board[temp_x][temp_y] == '0':
                board[temp_x][temp_y] = '1'


print('원래그림')
print(board)

for y in range(m):
    for x in range(n):
        if board[x][y] == 'q':
            check_q(x, y)
        elif board[x][y] == 'k':
            check_k(x, y)

print('변경그림')
print(board)

for _ in board:
    cnt += _.count('0')

print(cnt)
