n = int(input())

for i in range(n):
    j = int(input())
    dp = [0] * 12
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for k in range(4, j+1):
        dp[k] = dp[k-1] + dp[k-2] + dp[k-3]
    print(dp[j])
