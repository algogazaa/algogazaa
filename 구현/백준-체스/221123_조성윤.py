#
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
q = list(map(int, input().split()))
k = list(map(int, input().split()))
p = list(map(int, input().split()))
visited = [[False] * m for _ in range(n)]

def dfsQ(x,y,direction):
    visited[x][y] = True
    
    if direction == 1:
        return
    elif direction == 2:
        return
    elif direction == 3:
        return
    elif direction == 4:
        return
    elif direction == 5:
        return
    elif direction == 6:
        return
    elif direction == 7:
        return
    elif direction == 8:
        return