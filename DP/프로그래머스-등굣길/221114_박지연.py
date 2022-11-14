def solution(m, n, puddles):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1

    for j in range(m):
        if [1, j+1] not in puddles:
            dp[0][j] = 1

    for i in range(n):
        if [i+1, 1] not in puddles:
            dp[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if [i+1, j+1] not in puddles:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    print(dp)
    return dp[n-1][m-1]


# print(solution(4, 3, [[2,2]]))
# print(solution(3, 3, [[1, 3]]), 5) #5
# print(solution(3, 3, [[1, 3], [3, 1]]), 4) #4
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2) #2
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1) #1
print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) #이 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨