import copy
from collections import deque


def bfs(count, num_list):
    cut_num = count - 6
    q = deque()
    q.append([[], 0, cut_num])
    result = []

    while q:
        answer, index, cut_num = q.popleft()
        if len(answer) == 6:
            if answer not in result:
                result.append(answer)
        if index > count-1:
            continue
        if cut_num > 0:
            q.append([answer, index+1, cut_num-1])

        n_answer = copy.deepcopy(answer)
        n_answer.append(str(num_list[index]))
        q.append([n_answer, index+1, cut_num])

    return result

while True:
    g = list(map(int, input().split()))
    if len(g) == 1:
        break

    k = g[0]
    s = g[1:]

    if k == 0:
        break

    if k > len(s):
        continue
    result = bfs(k, s)
    result.sort()
    for i in result:
        print(' '.join(i))
    print()