N, M = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 1
cnt = 0

while end<=N:
    nums = numbers[start:end]
    sum_nums = sum(nums)

    if sum_nums == M:
        cnt += 1
        end += 1

    elif sum_nums < M:
        end += 1

    else:
        start += 1

print(cnt)
