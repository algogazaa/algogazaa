#
from collections import deque
def solution(begin, target, words):
	return bfs(begin, target, words)

def bfs(begin,target,words):
	q = deque([[begin, 0]])
	visited = [False] * len(words)
	while q:
		now, changeCnt = q.popleft()
		if now == target:
			return changeCnt

		for i in range(len(words)):
			if not visited[i]:
				cnt = 0
				for n, w in zip(now, words[i]):
					if n != w:
						cnt += 1
					if cnt == 2:
						break
				else:
					visited[i] = True
					q.append([words[i],changeCnt + 1])
	return 0

if __name__ == "__main__":
	begin = ["hit","hit"]
	target = ["cog","cog"]
	words = [["hot", "dot", "dog", "lot", "log", "cog"],["hot", "dot", "dog", "lot", "log"]]
	for a, b, c in zip(begin, target, words):
		print(solution(a,b,c))