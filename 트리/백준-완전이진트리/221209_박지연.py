import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
node = list(input().split())
answer = [[]for _ in range(n)]
q = deque()
q.append([node, 0])

while q:
    i, cnt = q.popleft()
    left, middle, right = i[:len(i)//2], i[len(i)//2], i[len(i)//2+1:]
    answer[cnt].append(middle)
    if len(left) != 1:
        q.append([left, cnt + 1])
        q.append([right, cnt + 1])
    else:
        answer[cnt+1].append(i[0])
        answer[cnt+1].append(i[2])

for i in answer:
    print(' '.join(i))