from collections import deque

def solution(numbers):
    answer = [-1 for _ in range(len(numbers))]

    for i in range(len(numbers)):
        bin_num = bin(numbers[i])[2:]
        j, k = 0, 0

        while True:
            if j >= len(bin_num):
                break
            j += 2**k
            k += 1

        if j - len(bin_num) > 1:
            answer[i] = 0
            continue
        else:
            bin_num = '0' * (j - len(bin_num)) + bin_num

        queue = deque()
        queue.append(bin_num)
        is_ok = True

        while queue:
            num = queue.popleft()
            left, middle, right = num[:len(num)//2], num[len(num)//2], num[len(num)//2+1:]
            if middle != '0':
                if len(left) >= 3:
                    queue.append(left)
                    queue.append(right)
            else:
                is_ok = False
                break

        if is_ok:
            answer[i] = 1
        else:
            answer[i] = 0

    return answer


print(solution([7, 5]), [1, 0])
print(solution([63, 111, 95]), [1, 1, 0])