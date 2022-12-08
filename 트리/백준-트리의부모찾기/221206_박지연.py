import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
node_list = []
for i in range(n-1):
    node_list.append(list(map(int, input().split())))
parent = [0 for _ in range(n+1)]

q = deque()
q.append(1)

while q:
    num = q.popleft()
    poplist = []
    for j in range(len(node_list)):
        if num in node_list[j]:
            poplist.append(j)
            if node_list[j][0] == num:
                parent[node_list[j][1]] = node_list[j][0]
                q.append(node_list[j][1])
            else:
                parent[node_list[j][0]] = node_list[j][1]
                q.append(node_list[j][0])
    poplist.sort(reverse=True)
    for i in poplist:
        node_list.pop(i)

for i in range(2, n+1):
    print(parent[i])