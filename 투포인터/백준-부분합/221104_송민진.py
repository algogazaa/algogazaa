import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))
min_length = float('inf')

right = 0
sum = arr[0]

for left in range(N):
    while sum < S and left <= right < N-1:
        right += 1
        sum += arr[right]

    if sum >= S:
        if min_length > right - left + 1:
            min_length = right - left + 1

    sum -= arr[left]

if min_length == float('inf'):
    print(0)

else:
    print(min_length)