my_numbers = [list(map(int, input().split())) for _ in range(5)]
bingo_board = [[False for _ in range(5)] for _ in range(5)]
called_numbers = []
for _ in range(5):
    called_numbers.extend(list(map(int, input().split())))

def update_bingo_board(num):
    for i in range(5):
        for j in range(5):
            if my_numbers[i][j] == num:
                bingo_board[i][j] = True
                return


def horizon_bingo():
    cnt = 0
    for row in bingo_board:
        if False not in row:
            cnt += 1
        else:
            continue
    return cnt


def vertical_bingo():
    cnt = 0
    for idx in range(5):
        for row in range(5):
            if bingo_board[row][idx] == False:
                break
            elif row == 4:
                cnt += 1
    return cnt


def cross_bingo():
    for idx in range(5):
        if bingo_board[idx][idx] == False:
            return 0
    return 1

def reverse_cross_bingo():
    reverse_idx = 4
    for row in range(5):
        if bingo_board[row][reverse_idx] == False:
            return 0
        else:
            reverse_idx -= 1
    return 1

trials = 0
three_bingo = False
bingo_cnt = 0
while not three_bingo:
    for num in called_numbers:
        trials += 1
        update_bingo_board(num)
        if horizon_bingo() + vertical_bingo() + cross_bingo() + reverse_cross_bingo() >= 3:
            three_bingo = True
            break


print(trials)
