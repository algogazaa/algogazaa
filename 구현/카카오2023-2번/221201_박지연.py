def solution(cap, n, deliveries, pickups):
    index = 0
    i = n - 1
    d_index = n - 1
    p_index = n - 1
    while True:
        while True:
            if deliveries[i] == 0 and pickups[i] == 0:
                if i < 0:
                    return index
                i -= 1
            else:
                break

        d_num = 0
        p_num = 0
        index += ((i + 1) * 2)

        while True:
            if d_num >= cap:
                break

            if d_index < 0:
                break

            if deliveries[d_index] < (cap - d_num):
                d_num += deliveries[d_index]
                deliveries[d_index] = 0
                d_index -= 1
            elif deliveries[d_index] == (cap - d_num):
                deliveries[d_index] = 0
                d_index -= 1
                break
            else:
                deliveries[d_index] -= cap - d_num
                break

        while True:
            if p_num >= cap:
                break

            if p_index < 0:
                break

            if pickups[p_index] < (cap - p_num):
                p_num += pickups[p_index]
                pickups[p_index] = 0
                p_index -= 1
            elif pickups[p_index] == (cap - p_num):
                pickups[p_index] = 0
                p_index -= 1
                break
            else:
                pickups[p_index] -= cap - p_num
                break

    return index


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))
