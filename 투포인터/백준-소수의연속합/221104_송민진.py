import math

N = int(input())
answer = 0

# 소수 구하기
primes = []
array = [True for _ in range(N + 1)]

for i in range(2, int(math.sqrt(N)) + 1):
    if array[i]:
        j = 2

        while i * j <= N:
            array[i * j] = False
            j += 1

for num in range(2, N + 1):
    if array[num]:
        primes.append(num)

if N == 1:
    print(0)
else:
    # 투포인터 합 구하기
    right = 0
    sum = 0

    for left in range(len(primes)):
        while sum < N and right < len(primes):
            sum += primes[right]
            right += 1

        if sum == N:
            answer += 1

        sum -= primes[left]

    print(answer)