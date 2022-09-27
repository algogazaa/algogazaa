n = int(input())
dasom = int(input())
candidates = [int(input()) for _ in range(n-1)]

answer = 0

if candidates:
    while dasom <= max(candidates):
        candidates[candidates.index(max(candidates))] -= 1
        dasom += 1
        answer += 1

print(answer)
