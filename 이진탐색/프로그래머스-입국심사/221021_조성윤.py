from tkinter import N


def solution(n, times):
    answer = 0
    start = 1
    end = n * max(times)
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for time in times:
            cnt += mid // time # 심사할 수 있는 인원수
            if cnt >=n:
                break
        if cnt >= n:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1
            
    return answer

if __name__ == "__main__":
    print(solution(6,[7,10]))