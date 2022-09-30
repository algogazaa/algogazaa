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

print(count)

# 2차시도 (런타임 에러)

# import heapq
# n = int(input())

# q = []

# for i in range(n):
#     start, end = map(int, input().split())
#     q.append([start, end])
#     print(q)

# q.sort()
# print('sort',q)

# room = []
# heapq.heappush(room, q[0][1])
# print('room',room)

# for i in range(1, n):
#     if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
#         heapq.heappush(room, q[i][1]) # 새로운 회의실 개설
#     else: # 현재 회의실에 이어서 회의 개최 가능
#         heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
#         heapq.heappush(room, q[i][1])

# print(len(room))


#1차 시도 (시간 초과)
# import heapq

# n=int(input())
# arr=[]
# for _ in range(n):
#     a,b,c=map(int,input().split())
#     heapq.heappush(arr,(b,c))


# brr=[] #사용한 튜플은 여기 담기
# cnt=0

# for i in range(len(arr)):
#     if arr[i] not in brr:
#         end=arr[i][1] #기준점 끝시간
#         brr.append(arr[i])

#         for j in range(i,len(arr)):
#             if end<=arr[j][0] and arr[j] not in brr: #끝시간과 앞시간 비교
#                 brr.append(arr[j])
#         cnt+=1


# print(cnt)
