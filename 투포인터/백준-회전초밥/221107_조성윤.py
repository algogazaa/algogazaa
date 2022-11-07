import sys
input = sys.stdin.readline
n,d,k,c = map(int, input().split())
sushi = []
for _ in range(n):
    sushi.append(int(input()))

sushi += sushi
start = 0
end = start + k
result = set()

while start < n:
    tempCase = set(sushi[start:end])
    if c not in tempCase:
        tempCase.add(c)
    if len(result) < len(tempCase):
        result = tempCase
    start += 1
    end = start + k

print(len(result))