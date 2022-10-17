from collections import deque

def bfs(q, word, target):

    while q:
        begin, cnt, pre_word = q.popleft()
        if begin == target:
            return cnt
        for i in word:
            result = 0
            if i != begin and i != pre_word:
                for j in range(len(i)):
                        if i[j] != begin[j]:
                            result += 1
            if result == 1:
                q.append([i, cnt+1, begin])

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0, ""])

    return bfs(queue, words, target)



a = ["hot", "dot", "dog", "lot", "log", "cog"]
b = ["hot", "dot", "dog", "lot", "log"]
# print(solution("hit", "cog", a))
print(solution("hit", "cog", b))