import itertools
from collections import deque
from collections import defaultdict
import copy
mov_r = [0, 0, -1, 1] # right left up down
mov_c = [1, -1, 0, 0]

def outofblock(x, y):
    return x>3 or y>3 or x<0 or y<0

# bfs
def how_many_times(board, current_position, position_to_move): 
    q = deque()
    new_current_position = current_position[:]
    new_current_position.append(0)
    q.append(new_current_position) # [1,0,0] 0-> 움직이는 횟수

    while q:
        r, c, k = q.popleft()

        if r == position_to_move[0] and c == position_to_move[1]:
            # print(f'return value : {k}')
            return k

        for i in range(4):
            # ctrl없이 이동
            new_r = r + mov_r[i]
            new_c = c + mov_c[i]
            if not outofblock(new_r, new_c):
                q.append([new_r, new_c, k+1])

            # ctrl로 이동
            flag = 0
            while(not outofblock(new_r, new_c) and board[new_r][new_c] == 0):
                flag = 1
                new_r += mov_r[i]
                new_c += mov_c[i]
                # print(f'newr, newc = {new_r, new_c}')
            if flag == 1:
                if outofblock(new_r, new_c):
                    q.append([new_r-mov_r[i], new_c-mov_c[i], k+1])
                else:
                    q.append([new_r, new_c, k+1])
    
    return -1

def solution(board, r, c):
    # print(board)
    d = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                d[board[i][j]].append([i,j])
    d = dict(d)
    card = d.keys()
    nPr = list(itertools.permutations(card, len(card)))

    answer_list = []
    for i in nPr:
        # print("-----------------------")
        # print(i)
        # dfs
        s = [[r,c,board,0,0]] # stack 0,0 -> cnt, numcard
        while s:
            temp = s.pop()
            if len(answer_list) != 0 and temp[3] >= min(answer_list):
                continue
            # print(f'temp : {temp}')
            # print(len(card))
            if temp[4] == len(card):
                answer_list.append(temp[3])
                continue

            j = i[temp[4]]
            
            # print(f'j : {j}')
            new_board1 = copy.deepcopy(temp[2])
            new_board2 = copy.deepcopy(temp[2])
            
            # A->B
            time1 = how_many_times(new_board1, [temp[0], temp[1]], d[j][0])
            new_board1[d[j][0][0]][d[j][0][1]] = 0
            time1 += how_many_times(new_board1, d[j][0], d[j][1])
            new_board1[d[j][1][0]][d[j][1][1]] = 0
            # print(f'append_array_value : {[d[j][1][0], d[j][1][1], new_board1, temp[3]+time1+2, temp[4]+1]}')
            s.append([d[j][1][0], d[j][1][1], new_board1, temp[3]+time1+2, temp[4]+1])

            # B->A
            time2 = how_many_times(new_board2, [temp[0], temp[1]], d[j][1])
            new_board2[d[j][1][0]][d[j][1][1]] = 0
            time2 += how_many_times(new_board2, d[j][1], d[j][0])
            new_board2[d[j][0][0]][d[j][0][1]] = 0
            #print(f'append_array_value : {[d[j][0][0], d[j][0][1], new_board2, temp[3]+time2+2, temp[4]+1]}')
            s.append([d[j][0][0], d[j][0][1], new_board2, temp[3]+time2+2, temp[4]+1])

    # print(answer_list)
    return min(answer_list)
if __name__ == "__main__":
    board = [[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]],[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]]
    r = [1,0]
    c = [0,1]
    for a,b,c in zip(board, r,c):
        print(solution(a,b,c))