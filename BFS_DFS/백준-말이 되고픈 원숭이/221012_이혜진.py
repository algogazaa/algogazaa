
#왜 틀림?
#참고:https://jae-eun-ai.tistory.com/39

from collections import deque

hdx = [-2,-2,-1,-1,1,1,2,2]
hdy = [-1,1,-2,2,-2,2,-1,1]
mdx=[-1,1,0,0]
mdy=[0,0,-1,1]

def bfs(x,y,k):
    que=deque()
    que.append((x,y,k))
    visit = [[[0 for _ in range(31)] for _ in range(m)] for _ in range(n)]
    while que:
        x,y,k=que.popleft()
        #마지막이면 끝내기
        if x==(n-1) and y==(m-1):
            return visit[x][y][k]
        #k 남아있을 땐 8방향 가능
        if k>0:
            for i in range(8):
                nx=x+hdx[i]
                ny=y+hdy[i]
                #공간 안& 처음 방문 & 갈 수 있는 길(0)
                if 0 <= nx < n and 0 <= ny < m and visit[nx][ny][k-1]==0 and g[ny][nx]==0:
                    visit[nx][ny][k-1]=visit[x][y][k]+1
                    que.append((nx,ny,k-1)) 

        for j in range(4):
            nx=x+mdx[j]
            ny=x+mdy[j] 
            #공간 안& 처음 방문 & 갈 수 있는 길(0)
            if 0 <= nx < n and 0 <= ny < m and visit[nx][ny][k]==0 and g[ny][nx]==0:
                visit[nx][ny][k]=visit[x][y][k]+1
                que.append((nx,ny,k)) 
    
    return -1


if __name__ == "__main__":
    k=int(input())
    m,n=map(int,input().split())
    g = [list(map(int,input().split())) for _ in range(n)]
    
    result=bfs(0,0,k)
    print(result)

