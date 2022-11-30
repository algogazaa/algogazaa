cap1 = 4
n1 = 5
deliveries1 = [1,0,3,1,2]
pickups1 = [0,3,0,4,0]

cap2 = 2
n2 = 7
deliveries2 = [1,0,2,0,1,0,2]
pickups2 = [0,2,0,1,0,2,0]


def solution(cap, n, deliveries, pickups):
    result = 0
    del_dist = {}
    pic_dist = {}
    cnt = 1
    longer = {}
    shorter = {}
    # 배달
    while len(deliveries) > 0:
        acc = 0
        # 남은 집 중 끝 집이 0 이라면 삭제
        while True:
            if deliveries[len(deliveries)-1] == 0:
                deliveries.pop()
            else:
                break
        del_dist[cnt] = len(deliveries)

        # 짐 최대 싣기
        while True:
            acc += deliveries[len(deliveries)-1]
            # 누적이 작으면 하나씩 줄이기
            if acc <= cap:
                deliveries = deliveries[0:-1]
                if len(deliveries) == 0:
                    break
            # 여유가 있었는데 다음게 초과한다면 일부만 배달
            else:
                deliveries[len(deliveries)-1] = acc-cap
                # print(deliveries)
                break
        cnt += 1
    # print('배달', del_dist)

    cnt = 1
    # 수거
    while len(pickups) > 0:
        acc = 0
        while True:
            if pickups[len(pickups)-1] == 0:
                pickups.pop()
            else:
                break
        pic_dist[cnt] = len(pickups)

        while True:
            acc += pickups[len(pickups) - 1]
            # 누적이 작으면 하나씩 줄이기
            if acc <= cap:
                pickups = pickups[0:-1]
                if len(pickups) == 0:
                    break
            # 여유가 있었는데 다음게 초과한다면 일부만 배달
            else:
                pickups[len(pickups) - 1] = acc - cap
                # print(pickups)
                break
        cnt += 1
    # print('수거', pic_dist)


    if len(del_dist) > len(pic_dist):
        longer = del_dist
        shorter = pic_dist
    else:
        longer = pic_dist
        shorter = del_dist

    for i in range(1, len(shorter)+1):
        longer[i] = max(del_dist[i], pic_dist[i])

    for j in range(1, len(longer)+1):
        result += longer[j]

    return result * 2

print(solution(cap2, n2, deliveries2, pickups2))
