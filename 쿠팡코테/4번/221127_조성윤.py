def solution(n, blocks):
    global board
    board = [[''] * n for _ in range(n)]
    for b in blocks:
        x,y = b
        board[x-1][y-1] = 'X'
    # X가 아닌 곳에서 시작하여 갈 수 있는 곳 True 처리
    
    # 
    return

def dfsBoard():
    global board
    
def dfsRook(start,end,size):
    global board
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    board[start][end] = 'K'
    
    for i in range(4):
        nx, ny = start, end
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < size and 0 <= ny < size:
                if board[nx][ny] == '':
                    board[nx][ny] = 'O'
            else:
                break

def dfsKnight(start,end,size):
    global board
    dx = [2,2,-2,-2,1,1,-1,-1]
    dy = [1,-1,1,-1,2,-2,2,-2]
    board[start][end] = 'K'
    
    for i in range(8):
        nx = start + dx[i]
        ny = end + dy[i]
        if 0 <= nx < size and 0 <= ny < size and board[nx][ny] == '':
            board[nx][ny] = 'O'

    
            
                
if __name__ == "__main__" :
    n = [3,4,2]
    blocks = [[[1,2],[2,1]],[[1,3],[1,4],[2,1],[2,2],[3,3],[3,4],[4,1],[4,2]], [[1,1]]]
    for a,b in zip(n, blocks):
        print(solution(a,b))