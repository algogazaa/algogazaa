import sys
input = sys.stdin.readline

n, d, k, c = list(map(int, input().split()))
rail = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
answer, end, cnt = 0, 0, 0
dic = {}

if c not in dic:
    dic[c] = 1
else:
    dic[c] += 1

for start in range(n):

    while cnt < k:
        if end >= n:
            end = end - n

        if rail[end] in dic:
            dic[rail[end]] += 1
        else:
            dic[rail[end]] = 1

        end += 1
        cnt += 1

    answer = max(answer, len(dic))

    if dic[rail[start]] == 1:
        del dic[rail[start]]
    else:
        dic[rail[start]] -= 1
    cnt -= 1

print(answer)