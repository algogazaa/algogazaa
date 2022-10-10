import copy
from collections import deque


def solution(n, info):
    answer = []
    max_num = 0
    result = []

    queue = deque()
    queue.append([result, 0, 0, 0])

    while queue:
        n_result, ssum, ap_sum, num = queue.popleft()
        if len(n_result) != len(info) and num != n:
            index = len(n_result)
            apeach = info[index]

            if index == len(info) -1:
                rrsult = copy.deepcopy(n_result)
                rrsult.append(n - num)
                queue.append([rrsult, ssum, ap_sum + 10 - index, num])
            else:

                if apeach != 0:
                    rrsult = copy.deepcopy(n_result)
                    rrsult.append(0)
                    queue.append([rrsult, ssum, ap_sum+10-index, num])
                    if num + apeach + 1 <= n:
                        rrsult = copy.deepcopy(n_result)
                        rrsult.append(apeach+1)
                        ssum += 10-index
                        num += apeach+1
                        queue.append([rrsult, ssum, ap_sum, num])
                else:
                    if num + 1 <= n:
                        rrsult = copy.deepcopy(n_result)
                        rrsult.append(1)
                        ssum += 10 - index
                        num += 1
                        queue.append([rrsult, ssum, ap_sum, num])
        else:
            if len(n_result) != len(info):
                for i in range(len(n_result), len(info)):
                    if info[i] != 0:
                        ap_sum += (10-i)
            if max_num < ssum - ap_sum:
                max_num = ssum - ap_sum
                answer = n_result

    while len(info) != len(answer):
        answer.append(0)

    if max_num == 0:
        return [-1]

    return answer


a = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
b = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
c = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
d = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]

print(solution(10, d))