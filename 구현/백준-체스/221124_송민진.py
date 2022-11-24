n, m = map(int, input().split())
q_tmp = list(map(int, input().split()))
k_tmp = list(map(int, input().split()))
p_tmp = list(map(int, input().split()))

map = [['0' for _ in range(m)] for _ in range(n)]

# knight
knights = []
while len(k_tmp) != 1:
    knights.append((k_tmp[1] - 1, k_tmp[2] - 1))
    k_tmp.remove(k_tmp[1])
    k_tmp.remove(k_tmp[1])

for knight in knights:
    map[knight[0]][knight[1]] = 'K'

# pawn
pawns = []
while len(p_tmp) != 1:
    pawns.append((p_tmp[1] - 1, p_tmp[2] - 1))
    p_tmp.remove(p_tmp[1])
    p_tmp.remove(p_tmp[1])

for pawn in pawns:
    map[pawn[0]][pawn[1]] = 'P'

# queen
queens = []
while len(q_tmp) != 1:
    queens.append((q_tmp[1] - 1, q_tmp[2] - 1))
    q_tmp.remove(q_tmp[1])
    q_tmp.remove(q_tmp[1])

for queen in queens:
    map[queen[0]][queen[1]] = 'Q'

for queen in queens:
    now_x, now_y = queen[0], queen[1]
    attacks = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for attack in attacks:
        new_x, new_y = now_x + attack[0], now_y + attack[1]
        while 0 <= new_x < n and 0 <= new_y < m and map[new_x][new_y] not in ['P', 'Q', 'K']:
            if map[new_x][new_y] == '0':
                map[new_x][new_y] = '1'
            new_x += attack[0]
            new_y += attack[1]

# knight
for knight in knights:
    now_x, now_y = knight[0], knight[1]
    attacks = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-2, 1), (-1, -2), (-2, -1)]
    for attack in attacks:
        new_x, new_y = now_x + attack[0], now_y + attack[1]
        if 0 <= new_x < n and 0 <= new_y < m and map[new_x][new_y] not in ['P', 'Q', 'K']:
            if map[new_x][new_y] == '0':
                map[new_x][new_y] = '1'

cnt = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == '0':
            cnt += 1

print(cnt)
