import sys
import heapq
input = sys.stdin.readline
l,r = input().split()

result = 0

if len(l) != len(r):
    print(0)

else:
    if l[0] != r[0]:
        print(0)
    else:
        if l[0] == '8':
            result += 1
        for i in range(1, len(l)):
            if l[i] != r[i]:
                break
            else:
                if l[i] == '8':
                    result += 1
        print(result)