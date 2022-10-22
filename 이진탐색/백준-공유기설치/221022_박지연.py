import sys
input = sys.stdin.readline
n, m = map(int, input().split())
house = []
for _ in range(n):
    house.append(int(input()))

house.sort()
start = 1
end = house[-1] - house[0]
answer = 1

while start <= end:
    mid = (start + end) // 2
    curHouse = house[0]
    cnt = 1
    for i in range(1,len(house)):
        if house[i] >= curHouse + mid:
            cnt += 1
            curHouse = house[i]

    if cnt >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)