# 시도 3 - 런타임 에러 (왜....?)
import sys
sys.setrecursionlimit(10*6)

def solution():
    input = sys.stdin.readline
    n = int(input())
    tree = [[] for _ in range(n+1)]
    sheep = {i: 0 for i in range(1, n + 1)}
    wolves = [0 for i in range(n + 1)]

    for i in range(2, n+1):
        animal_type, animal_cnt, parent = input().split()
        animal_cnt = int(animal_cnt)
        parent = int(parent)
        if animal_type == "S":
            sheep[i] = animal_cnt
        else:
            wolves[i] = animal_cnt
        tree[parent].append(i)

    def dfs(node):
        sheep_cnt = sheep[node]

        for child in tree[node]:
            sheep_cnt += dfs(child)

        if wolves[node] > 0:
            if sheep_cnt > wolves[node]:  # 양이 더 많을 경우, 늑대한테 먹힌 수만큼만 제외하기
                sheep_cnt -= wolves[node]
                wolves[node] = 0
            else:  # 늑대가 더 많을 경우, 이미 먹은 늑대들 제외하기
                wolves[node] -= sheep_cnt
                sheep_cnt = 0

        return sheep_cnt

    return dfs(1)


print(solution())




# 시도 3의 레퍼런스 - 얘는 성공 - 차이점을 모르겠음...,
# https://cocook.tistory.com/150

import sys

sys.setrecursionlimit(1000000)


def solution():
    input = sys.stdin.readline
    N = int(input())
    # wolves[i] : i번째 섬에 있는 늑대 수
    wolves = [0 for _ in range(N + 1)]

    # sheeps[i] : i번쨰 섬에 있는 양의 수=
    sheeps = {i: 0 for i in range(1, N + 1)}
    # 트리
    tree = [[] for _ in range(N + 1)]
    for i in range(2, N + 1):
        t, a, p = input().split()
        a = int(a)
        p = int(p)
        if t == "W":
            wolves[i] = a
        else:
            sheeps[i] = a

        tree[p].append(i)

    def dfs(here):
        num_sheeps = sheeps[here]

        for there in tree[here]:
            num_sheeps += dfs(there)  # 서브트리의 양들을 모두 더해준다.

        if wolves[here] != 0:  # 만약 현재 섬에 늑대가 있고
            if num_sheeps < wolves[here]:  # 서브트리의 양보다 현재 섬의 늑대가 많다면
                wolves[here] -= num_sheeps  # 배부른 늑대들이 줄어든다.
                num_sheeps = 0  # 양들은 모두 먹힘
            else:  # 양이 더 많다면
                num_sheeps -= wolves[here]  # 양이 줄어들고
                wolves[here] = 0  # 배부른 늑대는 0 이제부턴 이 섬은 동료들의 희생으로 그냥 지나갈 수 있다.

        return num_sheeps

    print(dfs(1))


solution()
