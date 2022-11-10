n = int(input())
stairs = [int(input()) for _ in range(n)]

dp = [0] * n

if len(stairs) <= 2:
    print(sum(stairs))

else:
    for i in range(n):

        if i == 0:
            dp[i] = stairs[i]

        elif i == 1:
            dp[i] = stairs[i-1] + stairs[i]

        else:
            dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])

    print(dp[-1])
