import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

end = 0
intervalSum = arr[0]
ans = float('inf')

for start in range(n):
    while intervalSum < m and end < n:
        end += 1
        if end == n:
            break
        intervalSum += arr[end]
    if intervalSum >= m:
        ans = min(ans, end - start + 1)
    intervalSum -= arr[start]

if ans == float('inf'):
    print(0)
else:
    print(ans)