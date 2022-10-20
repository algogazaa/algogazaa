#
import sys
input = sys.stdin.readline
n,m = map(int, input().split())
blue = list(map(int, input().split()))

start, end = sum(blue) // m, sum(blue)
answer = end
while start <= end:
    mid = (start + end) // 2
    
    if mid < max(blue):
        start = mid + 1
        continue
    
    # 조건 확인
    cnt, temp = 0, 0
    for i in range(len(blue)):
        if blue[i] > mid:
            break
        elif temp + blue[i] <= mid:
            temp += blue[i]
        else:
            temp = blue[i]
            cnt += 1
    
    if cnt <= m - 1:
        end = mid - 1
        answer = min(answer, mid)
    else:
        start = mid + 1

print(answer)