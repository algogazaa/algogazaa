n = int(input())
m = int(input())
node_list = [list(map(int, input().split())) for _ in range(m)]
visited = [False for _ in range(n)]

def dfs(index):
    visited[index-1] = True
    answer = 0
    for i in node_list:
        if visited[i[0]-1] and not visited[i[1]-1]:
            visited[i[1] - 1] = True
            answer += 1
            answer += dfs(i[1])
        elif not visited[i[0]-1] and visited[i[1]-1]:
            visited[i[0]-1] = True
            answer += 1
            answer += dfs(i[0])
    return answer

print(dfs(1))