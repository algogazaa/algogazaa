import sys
def solution(queue1, queue2):
    totalQ = queue1 + queue2
    targetNum = (sum(queue1) + sum(queue2))
    if targetNum % 2 == 0:
        targetNum //= 2
    else:
        return -1
    end = len(queue1) - 1
    sumNum = sum(queue1)
    result = 0
    
    for start in range(len(totalQ)):
        while end < len(totalQ):
            if sumNum == targetNum:
                return result
            elif sumNum < targetNum:
                if end == len(totalQ) -1:
                    return -1
                end += 1
                sumNum += totalQ[end]
                result += 1
            else:
                break
        sumNum -= totalQ[start]
        result += 1
        
    return -1

if __name__ == "__main__":
    q1 = [[3, 2, 7, 2],[1, 2, 1, 2],[1, 1]]
    q2 = [[4, 6, 5, 1],[1, 10, 1, 2],[1, 5]]
    for a,b in zip(q1, q2):
        print(solution(a,b))