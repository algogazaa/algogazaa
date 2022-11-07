import sys
input = sys.stdin.readline

N, d, k, coupon = map(int, input().split())
arr = list(int(input()) for _ in range(N))
max_types = 0
ate_list = []
ate_types = 0

right = 0
for left in range(N):
    while len(ate_list) < k:
        if right >= N:
            right = right - N
        ate_list.append(arr[right])
        right += 1

    ate_types = len(set(ate_list))
    if coupon not in ate_list:
        ate_types += 1

    max_types = max(max_types, ate_types)

    ate_list.remove(arr[left])

print(max_types)
