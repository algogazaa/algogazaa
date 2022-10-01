n = int(input())

classes = []

for _ in range(n):
    a, b = map(int, input().split())
    classes.append([int(b), int(a)])  # b = 끝나는시간, a = 시작하는 시간

classes.sort()

answer = 1
endtime = classes[0][0]
for i in range(1, len(classes)):
    if classes[i][1] >= endtime:
        answer += 1
        endtime = classes[i][0]
print(answer)