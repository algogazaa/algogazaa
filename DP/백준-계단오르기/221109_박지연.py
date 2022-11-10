import sys

n = int(input())
stairs = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

dp = [0] * n
dp[0] = stairs[0]
if len(stairs) == 2:
    dp[1] = max(stairs[0] + stairs[1], stairs[1])
if len(stairs) >= 3:
    dp[1] = max(stairs[0] + stairs[1], stairs[1])
    dp[2] = max(stairs[0] + stairs[2], stairs[2] + stairs[1])

for i in range(3, n):
    dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[n-1])