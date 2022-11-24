#
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
q = list(map(int, input().split()))
k = list(map(int, input().split()))
p = list(map(int, input().split()))
graph = [[False] * m for _ in range(n)]

def dfsQ(x,y,direction):
    