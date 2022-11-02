N, S = map(int, input().split())
numbers = list(map(int, input().split()))

start, end = 0, 1
min = N+1

sum_part = [0] * (N + 1)
for i in range(1, N + 1):
    sum_part[i] = sum_part[i-1] + numbers[i-1]

while end<=N:
    # if sum(numbers[start:end]) >= S:
    if sum_part[end] - sum_part[start] >= S:
        min = end - start
        start += 1

    else:
        end += 1
        if end - start >= min:
            start += 1
            
if min == N+1:
    print(0)
else:
    print(min)
