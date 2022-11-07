def solution(queue1, queue2):
    start, end, cnt = 0, 0, 0
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    if (sum1+sum2)%2 != 0:
        return -1

    while True:

        if sum1 == 0 or sum2 == 0:
            return -1

        if sum1 > sum2:
            sum1 -= queue1[start]
            sum2 += queue1[start]
            start += 1
            cnt += 1
        elif sum1 == sum2:
            return cnt
        else:
            sum1 += queue2[end]
            sum2 -= queue2[end]
            end += 1
            cnt += 1

        if start >= len(queue1):
            queue1 = queue2[:end]
            queue2 = queue2[end:] + queue1
            start, end = 0, 0
        elif end >= len(queue2):
            queue2 = queue1[:start]
            queue1 = queue1[start:] + queue2
            start, end = 0, 0


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))


from collections import deque

def solution2(queue1, queue2):
    answer = 0
    q1 = deque(queue1)
    q2 = deque(queue2)

    sum_q1 = sum(q1)
    sum_q2 = sum(q2)

    if (sum_q1 + sum_q2) % 2 != 0:
        return -1

    while True:
        if sum_q1 == sum_q2:
            return answer
        elif q1 == queue2 or sum_q1 == 0 or sum_q2 == 0:
            return -1
        elif sum_q1 > sum_q2:
            a = q1.popleft()
            sum_q1 -= a
            sum_q2 += a
            q2.append(a)
            answer += 1
        elif sum_q1 < sum_q2:
            a = q2.popleft()
            sum_q1 += a
            sum_q2 -= a
            q1.append(a)
            answer += 1

        # if answer == len(queue1) * 4:
        #     return -1
    return answer