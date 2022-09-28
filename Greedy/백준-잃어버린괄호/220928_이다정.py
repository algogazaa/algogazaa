div_minus = input().split('-')
answer = 0

for i in div_minus[0].split('+'):
    answer += int(i)

for j in div_minus[1:]:
    for k in j.split('+'):
        answer -= int(k)

print(answer)
