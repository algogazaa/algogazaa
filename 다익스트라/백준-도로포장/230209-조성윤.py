import sys
import heapq
INF = sys.maxsize
input = sys.stdin.readline
n,m,k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
# distance는 포장이 한번도 되지 않은 것부터, k개 된 거 까지 총 k + 1개가 필요하다.
distance = [[INF for _ in range(k + 1)] for _ in range(n + 1)]


for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
    graph[end].append((cost, start))

def dijkstra(start):
    cnt = 0 # 몇 번 포장했는지를 체크
    distance[start][cnt] = 0
    q = []
    heapq.heappush(q,(0,start,cnt))

    while q:
        dist, node, cnt = heapq.heappop(q)
        if dist > distance[node][cnt]:
            continue

        for info in graph[node]:
            # 현재 노드를 포장하지 않는 경우
            cost = dist + info[0]
            if cost < distance[info[1]][cnt]:
                distance[info[1]][cnt] = cost
                heapq.heappush(q, (cost, info[1], cnt))
            
            '''
            cnt가 k보다는 작아야하고, dist는 현재 노드의 cnt만큼 포장된 도로들의 최단 거리인데
            만약 현재 노드를 포장하는 경우 다음 노드의 최단 거리는 dist와 같아진다.
            그러므로 현재 노드를 포장한 뒤(현재 노드를 포장하였으므로 포장한 갯수는 cnt + 1이다.)
            다음 노드의 최단 거리와 같은 횟수 만큼(cnt + 1만큼) 포장한 다음 노드의 최단 거리를 비교 하였을 때,
            현재 노드를 포장해야 최단 거리가 더 작아진다면 해당 최단 거리 테이블을 갱신해준다.
            '''
            # 현재 노드를 포장하는 경우
            if cnt < k and distance[info[1]][cnt + 1] > dist:
                distance[info[1]][cnt + 1] = dist
                heapq.heappush(q, (dist, info[1], cnt + 1))

dijkstra(1)
print(min(distance[n]))