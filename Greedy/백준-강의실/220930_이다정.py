N = int(input())
times = [list(map(int, input().split(" "))) for _ in range(N)]
times.sort(key=lambda x:x[1])

answer = 0
end_time = 0

while len(times) > 0:
    answer += 1
    end_time = times.pop(0)[2]
    for lecture in times:
        if lecture[1] > end_time:
            end_time = times.pop(times.index(lecture))

print(answer)

###런타임 에러


N = int(input())
times = [list(map(int, input().split(" "))) for _ in range(N)]
times.sort(key=lambda x:x[1])

end = [0]

for lecture in times:
    end_early = min(end)
    if end_early < lecture[1]:
        end[end.index(end_early)] = lecture[2]
    else:
        end.append(lecture[2])

print(len(end))

### 시간 초과


import heapq

N = int(input())
times = [list(map(int, input().split(" "))) for _ in range(N)]
times.sort(key=lambda x:x[1])

q = []
first= times.pop(0)
heapq.heappush(q, first[2])

for i in times:
    if q[0] <= i[1]:
        heapq.heappop(q)
        heapq.heappush(q, i[2])
    else:
        heapq.heappush(q, i[2])

print(len(q))

### 구글링 (heapq 알고리즘)
