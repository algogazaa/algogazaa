def dfs(start,computers,visited,n):
    visited[start] = True
    for i in range(n):
        if i != start and computers[start][i] and not visited[i]:
            dfs(i, computers, visited,n)
            
def solution(n, computers):
    result = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited,n)
            result += 1
    return result

if __name__ == "__main__":
    n = [3,3]
    computers = [[[1, 1, 0], [1, 1, 0], [0, 0, 1]], [[1, 1, 0], [1, 1, 1], [0, 1, 1]]]
    for a, b in zip(n,computers):
        print(solution(a,b))