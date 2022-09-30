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