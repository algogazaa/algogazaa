n = int(input())
meetings = []

for _ in range(n):
    start, end = tuple(map(int, input().split()))
    meetings.append([start, end])

meetings.sort(key= lambda x:(x[1], x[0]))

latest_end = 0
cnt = 0

for s, e in meetings:
    if s >= latest_end:
        cnt += 1
        latest_end = e

print(cnt)
