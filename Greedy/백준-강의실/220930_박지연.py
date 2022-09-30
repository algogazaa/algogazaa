"""  시간초과

n = int(input())
lecture = []
for i in range(n):
    a, b, c = map(int, input().split())
    lecture.append([b,c])
lecture.sort()

result = []
j = 0
count = 0
while len(result) != len(lecture):
    if lecture[j] not in result:
        result.append(lecture[j])
        end_time = lecture[j][1]
        for k in range(j+1, len(lecture)):
            if lecture[k][0] >= end_time and lecture[k] not in result:
                result.append(lecture[k])
    count += 1
    j += 1

print(count)

"""
import heapq

n = int(input())
lecture = []
for i in range(n):
    a, b, c = map(int, input().split())
    lecture.append([b, c])
lecture.sort()

j = 0
count = 0
result = []

for i in lecture:
    if result and result[0] <= i[0]: # 가장 일찍 끝나는 시간보다 시작 시간이 크면
        heapq.heappop(result)       # result 가장 작은 원소 pop & return
    heapq.heappush(result, i[1])    # result i[1]=끝나는 시간을 추가

print(len(result))
