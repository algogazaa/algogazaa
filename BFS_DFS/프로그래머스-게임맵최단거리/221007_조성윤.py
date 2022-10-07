from collections import deque
def solution(maps):
    answer = 0
    lenx = len(maps)
    leny = len(maps[0])
    bfs([0,0],lenx,leny,maps)
    
    if maps[-1][-1] != 1:
        return maps[-1][-1]
    else:
        return -1

def bfs(start,lenx,leny,maps):
    q = deque([start])
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < lenx and 0 <= ny < leny and not(nx == 0 and ny == 0) and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                q.append([nx,ny])
        

if __name__ == "__main__":
    maps = [[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]],[[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]]
    for m in maps:
        print(solution(m))