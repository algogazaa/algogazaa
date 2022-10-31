from collections import deque
def solution(music):
    global visited
    piano = {
        1: [2,3],
        2: [1,3],
        3: [1,2,4,5],
        4: [3,5],
        5: [3,4,6,7],
        6: [5,7],
        7: [5,6,8],
        8: [7,9,10],
        9: [8,10],
        10: [8,9,11,12],
        11: [10,12],
        12: [10,11]
    }
    result = 0
    start = 1
    for m in music:
        visited = [0] * 13
        result += bfs(piano, start, m)
        start = m
    
    return result
        
        

def bfs(piano, start, target):
    global visited
    q = deque([start])
    while q:
        num = q.popleft()
        if num == target:
            return visited[num]
        for nextN in piano[num]:
            if not visited[nextN]:
                visited[nextN] += visited[num] + 1
                q.append(nextN)
                
        
print(solution([10,9,4,5,12]))
print(solution([6,4,2,11]))