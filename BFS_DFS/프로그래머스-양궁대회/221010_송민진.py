# 경우 1 : Combinations with replacement 사용
from itertools import combinations_with_replacement

def solution(n, info):
    answer = [-1]
    max_gap = -1  # 점수 차

    # 중복 조합으로 0 ~ 10점까지 n개 뽑기
    for comb in combinations_with_replacement(range(11), n):
        arrows = [0] * 11
        for i in comb:
            arrows[10 - i] += 1

        apeach_score, ryan_score = 0, 0
        for idx in range(11):
            # 라이언과 어피치 모두 한번도 화살을 맞히지 못한 경우
            if info[idx] == arrows[idx] == 0:
                continue
            # 어피치가 라이언이 쏜 화살의 수 이상을 맞힌 경우
            elif info[idx] >= arrows[idx]:
                apeach_score += 10 - idx
            # 라이언이 어피치보다 많은 수의 화살을 맞힌 경우
            else:
                ryan_score += 10 - idx

        # 라이언이 점수가 더 높은 경우, 점수차 구해서 최대점수차일 때를 찾기
        if ryan_score > apeach_score:
            gap = ryan_score - apeach_score
            if gap > max_gap:
                max_gap = gap
                answer = arrows
    return answer


  
# 경우 2 : BFS 사용
from collections import deque

def solution(n, info):
    win_list = bfs(n, info)

    # 이길 수 있는 경우가 없으면,
    if not win_list:
        return [-1]

    # 이기는 경우가 하나밖에 없으면, 그대로 출력
    elif len(win_list) == 1:
        return win_list[0]

    # 이기는 경우가 여러개일 때, 우선순위대로 출력
    else:
        return win_list[-1]

def bfs(n, info):
    arrows = []
    max_gap = 0

    queue = deque()
    queue.append((0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

    while queue:
        focus, arrow = queue.popleft()

        # 화살을 다 쏜 경우, 점수 계산하기
        if sum(arrow) == n:
            apeach_score, ryan_score = 0, 0
            for i in range(11):
                if not (info[i] == arrow[i] == 0):
                    if info[i] >= arrow[i]:
                        apeach_score += 10 - i
                    else:
                        ryan_score += 10 - i

            # 총점 계산 결과 : 라이언이 이긴 경우, 최대 점수차 경우 도출
            if ryan_score > apeach_score:
                gap = ryan_score - apeach_score
                if gap > max_gap:
                    max_gap = gap
                    arrows.clear()
                else:
                    continue
                arrows.append(arrow)

        # 화살을 더 쏜 경우, 반복문 넘기기
        elif sum(arrow) > n:
            continue

        # 10점 과녁까지 왔는데 화살을 아직 덜 쏜 경우, 남은 화살을 마지막 과녁(10점) 몰빵
        elif focus == 10:
            tmp = arrow.copy()
            tmp[focus] = n - sum(tmp)
            queue.append((-1, tmp))

        # 화살 쏘기
        else:
            # 경우 1 : 어피치보다 1발 많이 쏘기
            tmp = arrow.copy()
            tmp[focus] = info[focus] + 1
            queue.append((focus + 1, tmp))

            # 경우 2 : 0발 쏘기
            tmp2 = arrow.copy()
            tmp2[focus] = 0
            queue.append((focus + 1, tmp2))

    return arrows
