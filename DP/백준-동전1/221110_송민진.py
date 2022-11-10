n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)    # dp[i] = i원을 만들 때 가능한 경우의 수
dp[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        dp[i] += dp[i - coin]

print(dp[k])
