def dfs(lionList, info, n, depthIdx):
    global answers, maxSumScore
    # 화살을 다 쏜 경우
    if n == 0:
        score = 0
        for (idx, l) in enumerate(lionList):
            if l != 0:
                score += 10 - idx
        if score > maxSumScore:
            maxSumScore = score
            answers = []
            answers.append(lionList)
        elif score == maxSumScore:
    # 맞추는 경우
    
    # 못 맞추는 경우

def solution(n, info):
    global answers, maxSumScore
    maxSumScore = 0
    answers = []
    return
if __name__ == "__main__":
    n = [4,1,9,10]
    info = [[2,1,1,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0],[0,0,1,2,0,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,3,4,3]]
    print(solution(a,b))