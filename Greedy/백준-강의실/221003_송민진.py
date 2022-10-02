import heapq

n = int(input())
lecture_list = []

for _ in range(n):
    num, start, end = map(int, input().split())
    lecture_list.append([start, end])
lecture_list.sort()

min_heap = []
heapq.heappush(min_heap, lecture_list[0][1])

for i in range(1, n):
    current_start = lecture_list[i][0]
    current_end = lecture_list[i][1]
    fastest_end = min_heap[0]

    if current_start >= fastest_end:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, current_end)

print(len(min_heap))
