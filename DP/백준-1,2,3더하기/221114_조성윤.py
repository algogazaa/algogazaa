#
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    target = int(input())
    dp = [0,1,2,4] + [0] * (target - 3)
    for i in range(4, target + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    print(dp[target])