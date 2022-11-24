cheolsu = dict()
numbers = []
call_num = []

for i in range(5):
    numbers = list(map(int, input().split()))
    for j in range(5):
        cheolsu[numbers[j]] = (i, j)

for _ in range(5):
    call_num.extend(list(map(int, input().split())))

bingo = {'h0':0, 'h1':0, 'h2':0, 'h3':0, 'h4':0, 'v0':0, 'v1':0, 'v2':0, 'v3':0, 'v4':0, 'dl':0, 'dr':0}

def cnt_bingo(num):
    loc = cheolsu[num]
    x, y = loc[0], loc[1]
    bingo['h'+str(x)] += 1
    bingo['v'+str(y)] += 1
    if(x == y):
        bingo['dl'] += 1
    if (4-x == y):
        bingo['dr'] += 1
    return list(bingo.values()).count(5)
    # print(num,'의 빙고판',list(bingo.values()).count(5))


for cnt, num in enumerate(call_num):
    if cnt_bingo(num) > 2:
        print(cnt + 1)
        break
