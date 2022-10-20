def solution(n, times):
    answer = max(times) * n
    start = 1
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2
        time, cnt = 0, 0
        time_list = []
        m = 0
        for i in times:
            for j in range(m, n+1):
                if time + i <= mid:
                    time += i
                    if j == n-1:
                        time_list.append(time)
                else:
                    time_list.append(time)
                    time = 0
                    m = j + 1
                    cnt += 1
                    break

        if cnt >= len(times):
            start = mid + 1
        else:
            answer = min(answer, max(time_list))
            end = mid - 1

    return answer


print(solution(10, [2, 10]))