from collections import deque


def solution(queue1, queue2):
    min_action = float('inf')

    q1 = deque(queue1)
    q2 = deque(queue2)
    half = (sum(queue1) + sum(queue2)) / 2
    q1_sum = sum(queue1)

    action = 0
    while True:

        if q1_sum == half:
            break

        elif q1_sum > half:
            num = q1.popleft()
            q2.append(num)
            action += 1
            q1_sum -= num

        else:
            num = q2.popleft()
            q1.append(num)
            action += 1
            q1_sum += num

        if action >= (len(q1) + len(q2)) * 2:  # 범위 설정 관련 -> 마지막 반례 참고
            break

    if q1_sum == half:
        min_action = min(min_action, action)

    if min_action == float('inf'):
        min_action = -1

    return min_action


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
print(solution([1, 1, 1, 1, 1], [1, 1, 1, 9, 1]))  # 기댓값 12 / 합친 길이 이상으로 숫자를 이동할 수 있는게 핵심!
