N = int(input())
times = [list(map(int, input().split(" "))) for _ in range(N)]
times.sort(key=lambda x:(x[1],x[0]))

end = 0
cnt = 0
for x in times:
    if end <= x[0]:
        end = x[1]
        cnt += 1

print(cnt)
