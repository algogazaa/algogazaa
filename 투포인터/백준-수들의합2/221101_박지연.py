import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
num = list(map(int, input().split()))

num_sum = 0
end = 0
count = 0

for start in range(n):

    while num_sum < m and end < n:
        num_sum += num[end]
        end += 1

    if num_sum == m:
        count += 1

    num_sum -= num[start]

print(count)