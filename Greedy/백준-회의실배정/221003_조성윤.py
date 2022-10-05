import sys
n = int(sys.stdin.readline())
meet = []
for _ in range(n):
    meet.append(list(map(int, sys.stdin.readline().split())))

meet.sort(key = lambda x:[x[1],x[0]])

cnt = 1
start = meet[0]
for i in range(1,len(meet)):
    if meet[i][0] < start[1]:
        continue
    cnt += 1
    start = meet[i]

print(cnt)