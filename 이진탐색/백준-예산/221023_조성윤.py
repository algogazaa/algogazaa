#
import sys
input = sys.stdin.readline
n = int(input())
budget = list(map(int, input().split()))
limit = int(input())
answer = 0
start = 1
end = max(budget)

while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for b in budget:
        if b >= mid:
            temp += mid
        else:
            temp += b
    
    if temp == limit:
        print(mid)
        break
    if temp < limit:
        start = mid + 1
    else:
        end = mid - 1
else:
    print(end)
        