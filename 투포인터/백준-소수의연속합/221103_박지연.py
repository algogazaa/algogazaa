import math

n = int(input())
array = [True for _ in range(n+1)]
num = []
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i]:
        j = 2

        while i * j <= n:
            array[i*j] = False
            j += 1

for j in range(2, n+1):
    if array[j]:
        num.append(j)

end, cnt, num_sum = 0, 0, 0

for start in range(len(num)):
    while num_sum < n and end < len(num):
        num_sum += num[end]
        end += 1

    if num_sum == n:
        cnt += 1

    num_sum -= num[start]

print(cnt)