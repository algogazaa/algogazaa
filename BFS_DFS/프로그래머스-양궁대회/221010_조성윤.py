from copy import deepcopy
def dfs(lionList, info, n, depthIdx):
    global answers, maxSumScore
    # 화살을 다 쏜 경우
    if depthIdx == 11:
        if n!= 0:
            lionList[10] = n
        
        # 점수 계산
        score = 0
        for (idx, l) in enumerate(lionList):
            if lionList[idx] != 0:
                score += 10 - idx
        
        if score <= 0: # s
            return
        temp = deepcopy(lionList)
        if score > maxSumScore:
            maxSumScore = score
            answers = [temp]
                
        
            
    # 맞추는 경우
        if info[depthIdx] < n:
            lionList.append(info[depthIdx] + 1)
            dfs(info, lionList, n - info[depthIdx] - 1, depthIdx + 1)
            lionList.pop()
            
    # 못 맞추는 경우
    lionList.append(0)
    dfs(info, lionList, n, depthIdx + 1)
    lionList.pop()

def solution(n, info):
    global answers, maxSumScore
    maxSumScore = 0
    answers = []
    dfs(info, [], n, 0)
    if answers == []:
        return [-1]
    answers.sort(key = lambda x : x[::-1], reverse=True)
    
    return answers[0]
if __name__ == "__main__":
    n = [4,1,9,10]
    info = [[2,1,1,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0,0],[0,0,1,2,0,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,3,4,3]]
    print(solution(a,b))