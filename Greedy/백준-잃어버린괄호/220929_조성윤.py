import sys
strings = sys.stdin.readline().rstrip().split('-')
num = []

for string in strings:
    cnt = 0
    temp = string.split('+')
    for j in temp:
        cnt += int(j)
    num.append(cnt)

result = num[0]
for i in range(1, len(num)):
    result -= num[i]

print(result)