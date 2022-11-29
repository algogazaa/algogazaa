import copy

n1 = 3
blocks1 = [[1,2],[2,1]]

n2 = 4
blocks2 = [[1,3],[1,4],[2,1],[2,2],[3,3],[3,4],[4,1],[4,2]]

n3 = 2
blocks3 = [[1,1]]

rx = [-2,-1,1,2,2,1,-1,-2]
ry = [-1,-2,-2,-1,1,2,2,1]


def check_case(x, y, board, cnt, result): # 돌면서 남아있는 것중에 계속 지우면서 거름
    remains = 0
    temp_board = copy.deepcopy(board)

    if cnt == len(board):
        for i in range(len(board)):
            for j in range(len(board)):
                if temp_board[i][j] == '.':
                    temp_board[i][j] = 'X'
                    result += 1
                    # print(cnt,"번째끝내기", temp_board, result)
        return temp_board, result

    for a in range(8):
        if 0 <= x + rx[a] < len(board) and 0 < y + ry[a] < len(board):
            temp_board[x + rx[a]][y + ry[a]] = 'X'
    for b in range(len(board)):
        temp_board[x][b] = 'X'
        temp_board[b][y] = 'X'

    # print("현재", cnt, "번째", x, y, '에서', temp_board)

    for line in temp_board:
        for _ in line:
            remains += _.count('.')

    if remains >= len(board) - cnt:
        # 다음 것 찾기
        for i in range(len(board)):
            for j in range(len(board)):
                if temp_board[i][j] != 'X':
                    cnt += 1
                    temp_board, result = check_case(i, j, temp_board, cnt, result)

    return temp_board, result


def solution(n, blocks):
    result = 0

    board = [['.' for _ in range(n)] for _ in range(n)]

    for spot in blocks:
        board[spot[0]-1][spot[1]-1] = 'X'

    for i in range(n):
        for j in range(n):
            if board[i][j] == '.':
                board[i][j] = 'X'
                temp_board, result = check_case(i, j, board, 1, result)

    return result

print(solution(n1, blocks1))
