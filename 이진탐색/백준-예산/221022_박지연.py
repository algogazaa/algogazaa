import sys
input = sys.stdin.readline

n = int(input())
region = list(map(int, input().split()))
max_num = int(input())

start = 1
end = max_num
answer = start

if max_num >= sum(region):
    answer = max(region)
else:
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in region:
            if i > mid:
                cnt += mid
            else:
                cnt += i

        if cnt > max_num:
            end = mid - 1
        else:
            answer = max(answer, mid)
            start = mid + 1

print(answer)