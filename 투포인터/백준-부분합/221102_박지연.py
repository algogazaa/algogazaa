import sys
input = sys.stdin.readline

n, s = list(map(int, input().split()))
num = list(map(int, input().split()))

end = 0
min_length = sys.maxsize
num_sum = 0

for start in range(n):

    while end < n and num_sum < s:
        num_sum += num[end]
        end += 1

    if num_sum >= s:
        if end == start:
            min_length = min(min_length, end-start+1)
        else:
            min_length = min(min_length, end-start)

    num_sum -= num[start]

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)