def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)]

    for com in range(n):
        if visited[com] == False:
            dfs(com, computers, visited)
            answer += 1
    return answer


def dfs(com, computers, visited):
        visited[com] = True
        for other in range(len(computers[com])):
            if computers[com][other] == 1 and com != other:
                if visited[other] == False:
                    dfs(other, computers, visited)
