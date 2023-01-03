#
import sys
sys.setrecursionlimit(10**6)
from collections import defaultdict
input = sys.stdin.readline
n = int(input())
tree = defaultdict(list)
parent = [0  for i in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(n - 1):
	start, end = map(int, input().split())
	tree[start].append(end)
	tree[end].append(start)

def dfs(parentNode):
	visited[parentNode] = True
	for i in tree[parentNode]:
		if not visited[i]:
			parent[i] = parentNode 
			dfs(i)

dfs(1)
for i in range(2,n + 1):
	print(parent[i])