import sys
input = sys.stdin.readline

n, d, k, c = list(map(int, input().split()))
rail = [int(sys.stdin.readline().rstrip()) for _ in range(n)]

is_c = False

for start in range(n):
    for end in range(start, start+4):

        if end >= n:
            end = end - n + 1

        if rail[end] == c:
            is_c = True
            start = end + 1
            break
    else:
        print(k+1)
        break
else:
    print(k)