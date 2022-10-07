def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]

    for com in range(n):
        if visited[com] == False:
            DFS(n, computers, com, visited)
            answer += 1

    return answer

def DFS(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n, computers, connect, visited)


a = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
b = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]