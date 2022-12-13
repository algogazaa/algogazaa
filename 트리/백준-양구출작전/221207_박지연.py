import sys

input = sys.stdin.readline
n = int(input())
num = [0 for _ in range(n+1)]
node = []
for i in range(n-1):
    node.append([i+2]+list(input().split()))
    if node[i][1] == 'S':
        num[i+2] = int(node[i][2])
    else:
        num[i + 2] = int(node[i][2]) * -1

node.sort(key = lambda x :(x[3]))
for j in reversed(range(n-1)):
    if node[j][3] == '1':
        if num[node[j][0]] >= 0:
            num[1] += num[node[j][0]]
    else:
        if num[node[j][0]] >= 0:
            num[int(node[j][3])] += num[node[j][0]]

print(num[1])