import heapq

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x:x[1]) # 시작 시간으로 오름차순 정렬

min_heap = [] #끝나는 시간만 들어감, 1세트씩
count = 0

#다른 수업 시간과 겹치지 않으면 이전 수업 pop
for other in arr:
    while min_heap and min_heap[0]<=other[1]: #끝나는시간 <=다른 강의 시작 시간
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, other[2]) 
    count = max(count, len(min_heap))
