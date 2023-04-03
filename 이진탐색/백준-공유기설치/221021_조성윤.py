#
import sys
input = sys.stdin.readline
n,c = map(int, input().split())
wifi = []
for _ in range(n):
    wifi.append(int(input()))
wifi.sort()

start = 1
end = wifi[-1] - wifi[0]
result = 0

while start <= end:
    mid = (start + end) // 2
    curHouse = wifi[0]
    cnt = 1
    
    for i in range(1,len(wifi)):
        if wifi[i] >= curHouse + mid:
            cnt += 1
            curHouse = wifi[i]
    
    if cnt >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)