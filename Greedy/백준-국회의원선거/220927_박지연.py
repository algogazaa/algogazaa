n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

count = 0

while True:
    max_num = max(num)
    if max_num == num[0] and num.count(max_num) == 1:
        print(count)
        break
    elif max_num == num[0] and num.count(max_num) > 1:
        count += 1
        print(count)
        break
    else:
        index = num.index(max_num)
        num[index] -= 1
        num[0] += 1
        count += 1