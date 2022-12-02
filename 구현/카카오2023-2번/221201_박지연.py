def solution(cap, n, deliveries, pickups):
    answer = 0
    d_cnt, p_cnt = 0, 0
    visited = []

    for i in reversed(range(n)):
        if deliveries[i] != 0:
            visited.append(i+1)
            d_cnt += deliveries[i]
        if pickups[i] != 0:
            visited.append(i+1)
            p_cnt += pickups[i]

        if d_cnt > cap or p_cnt > cap:
            answer += max(visited) * 2
            visited = []
            if d_cnt > cap:
                visited.append(i+1)
                d_cnt -= cap
            else:
                d_cnt = 0
            if p_cnt > cap:
                visited.append(i+1)
                p_cnt -= cap
            else:
                p_cnt = 0

        if i == 0 and len(visited) != 0:
            answer += max(visited) * 2
    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
