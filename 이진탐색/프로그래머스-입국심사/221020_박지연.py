def solution(n, times):
    answer = max(times) * n
    start = 1
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2
        time, cnt = 0, 0
        for i in times:
            cnt += mid//i

        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    return answer


print(solution(6, [7, 10]))