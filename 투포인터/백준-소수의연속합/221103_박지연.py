import math

n = int(input())
num = []

def isPrime(a):
    for j in range(2, int(math.sqrt(a))+1):
        if a % j == 0:
            return False
    return True


for i in range(2, n):
    if isPrime(i):
        num.append(i)
    if num[len(num)-2] + i > n:
        break

end, cnt, num_sum = 0, 0, 0

for start in range(len(num)):
    while num_sum < n and end < len(num):
        num_sum += num[end]
        end += 1

    if num_sum == n:
        cnt += 1

    num_sum -= num[start]

if isPrime(n):
    cnt += 1
print(cnt)