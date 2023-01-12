import sys
import heapq

INF = sys.maxsize

def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]
    for a,b,c in road:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    tableList = dijkstra(1, graph, N)
    print(tableList)
    for i in range(1,len(tableList)):
        if tableList[i] <= K:
            answer += 1

    return answer

def dijkstra(start, graph, N):
    q = []
    distance = [INF for _ in range(N + 1)] # 최단 거리 테이블
    distance[start] = 0
    heapq.heappush(q, (0,start)) # dist, node 위치 저장
    
    while q:
        dist, node = heapq.heappop(q)
        # 이미 해당 node를 체크해봤다면 패스
        if distance[node] < dist:
            continue
        # 해당 node와 연결된 node들의 최단거리 테이블 갱신
        for nextNode in graph[node]:
            cost = dist + nextNode[1]
            if cost < distance[nextNode[0]]:
                distance[nextNode[0]] = cost
                heapq.heappush(q,(cost, nextNode[0]))
        
    return distance

if __name__ == "__main__":
    N = [5,6]
    road = [[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]]
    K = [3,4]
    for a,b,c in zip(N,road,K):
        print(solution(a,b,c))