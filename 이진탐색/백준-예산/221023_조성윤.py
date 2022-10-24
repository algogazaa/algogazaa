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
    
    if temp >= limit:
        end = mid - 1
        answer = mid
    else:
        start = mid + 1

print(answer)
        