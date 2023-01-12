import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    distance = [INF for _ in range(n + 1)]
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for nextNode in graph[now]:
            cost = dist + nextNode[1]
            if cost < distance[nextNode[0]]:
                distance[nextNode[0]] = cost
                heapq.heappush(q, (cost, nextNode[0]))
                
    return distance

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
start, end = map(int, input().split())

print(dijkstra(start)[end])