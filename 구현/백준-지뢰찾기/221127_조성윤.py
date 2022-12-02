#
import sys
input = sys.stdin.readline
n = int(input())
mineGraph = [list(input().rstrip()) for _ in range(n)]
openGraph = [list(input().rstrip()) for _ in range(n)]
findMine = False

dx = [0,0,1,-1,1,-1,-1,1]
dy = [1,-1,0,0,1,-1,1,-1]
for x in range(n):
    for y in range(n):
        if openGraph[x][y] == "x":
            # 만약 x칸인데 지뢰라면
            if mineGraph[x][y] == "*":
                findMine = True
                continue
            
            cnt = 0
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if mineGraph[nx][ny] == "*":
                        cnt += 1
            openGraph[x][y] = str(cnt)

if findMine:
    for x in range(n):
        for y in range(n):
            if mineGraph[x][y] == "*":
                openGraph[x][y] = "*"
                
for o in openGraph:
    print(''.join(o))
