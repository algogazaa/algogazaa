def solution(cap, n, deliveries, pickups):
    cnt = 0
    all_delivered = False
    all_pickuped = False

    while all_delivered == False or all_pickuped == False:
        farthest_house = 0

        # 짐을 실어다줄 가장 먼 집까지의 거리 구하기 + 최대로 짐 실어가기
        truck_space = 0
        if max(deliveries) == 0:
            all_delivered = True
        else:
            for house in reversed(range(n)):
                delivery = deliveries[house]
                if delivery != 0 and truck_space + delivery <= cap:
                    truck_space += delivery
                    deliveries[house] = 0
                    farthest_house = house

        # 짐을 수거할 가장 먼 집까지의 거리 구하기 + 최대로 짐 실어오기
        truck_space = 0
        if max(pickups) == 0:
            all_pickuped = True
        else:
            for house in reversed(range(n)):
                pickup = pickups[house]
                if pickup != 0 and truck_space + pickup <= cap:
                    truck_space += pickup
                    pickups[house] = 0
                    farthest_house = max(farthest_house, house)

        cnt += (farthest_house + 1) * 2

    return cnt
