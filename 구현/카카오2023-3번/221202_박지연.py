from itertools import *

def solution(users, emoticons):
    answer = [0, 0]
    dis = [10, 20, 30, 40]
    # type = []
    # for i in range(1, 5):
    #     type += [i*10] * len(emoticons)

    real_list = list(product(dis, repeat = len(emoticons)))
    # real_list = set(printList)

    for i in real_list:
        join_num = 0
        discount_emo = [0 for _ in range(len(emoticons))]
        price = [0 for _ in range(len(users))]
        for j in range(len(i)):
            discount_emo[j] = emoticons[j] * (100 - i[j]) // 100
            for k in range(len(users)):
                if i[j] >= users[k][0]:
                    price[k] += discount_emo[j]

        for p in range(len(price)):
            if users[p][1] <= price[p]:
                price[p] = 0
                join_num += 1

        if join_num > answer[0]:
            answer[0] = join_num
            answer[1] = sum(price)
        elif join_num == answer[0] and answer[1] < sum(price):
            answer[1] = sum(price)

    return answer


# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900],
                [40, 3100], [27, 9200],[32, 6900]], [1300, 1500, 1600, 4900]))