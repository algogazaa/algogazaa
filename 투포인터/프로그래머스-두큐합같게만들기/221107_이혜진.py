from collections import deque


def solution(queue1, queue2):
    q1=deque(queue1)
    q2=deque(queue2)
    half=(sum(queue1)+sum(queue2))/2
    tmp1=sum(queue1)

    for i in range(300000):
        if tmp1 == half:
            return i
        elif tmp1 > half:
            num = q1.popleft()
            q2.append(num)
            tmp1 -= num
        else: # q2_sum이 q1_sum보다 클 때
            num = q2.popleft()
            q1.append(num)
            tmp1 += num      
    return -1 # 값이 같아지지 않으면 -1을 반환

if __name__ == '__main__':
    print(solution([3, 2, 7, 2],[4, 6, 5, 1]))
    print(solution([1, 2, 1, 2],[1, 10, 1, 2]))
    print(solution([1, 1],[1,5]))
