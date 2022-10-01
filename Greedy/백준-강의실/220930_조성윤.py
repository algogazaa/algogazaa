import sys
input = sys.stdin.readline
n = input()
room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

room.sort(key = lambda x: x[1])
minHeap = []
