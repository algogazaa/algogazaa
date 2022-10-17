#
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start, result):
	if len(result) == 6:
		print(*result)
	for i in range(start, len_S):
		result.append(S[i])
		dfs(i + 1,result)
		result.pop()

while True:
	S = list(map(int, input().split()))
	if S[0] == 0:
		break
	len_S = S[0]
	S = S[1:]
	dfs(0,[])
	print()