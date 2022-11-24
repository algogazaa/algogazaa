from collections import deque
def solution(data):
    q = deque(data)
    waitingDoc = []
    startDoc = q.popleft()
    curTime = startDoc[1] + startDoc[2]
    result = [startDoc[0]]
    while len(result) != len(data) and q:
        while q and curTime >= q[0][1]:
            waitingDoc.append(q.popleft())
        
        if q and not waitingDoc: # 한 개도 안들어 있는 경우
            excutePrintTarget = q.popleft()
            curTime = excutePrintTarget[2] + excutePrintTarget[1]
            result.append(excutePrintTarget[0])
            continue
            
        waitingDoc.sort(key = lambda x : x[2])
        excutePrintTarget = waitingDoc.pop(0)
        curTime += excutePrintTarget[2]
        result.append(excutePrintTarget[0])
    
    while waitingDoc:
        result.append(waitingDoc.pop(0)[0])
    return result

if __name__ == "__main__":
    data = [[[1,0,5],[2,2,2],[3,3,1],[4,4,1],[5,10,2]],[[1,0,3],[2,1,3],[3,3,2],[4,9,1],[5,10,2]],[[1,2,10],[2,5,8],[3,6,9],[4,20,6],[5,25,5]]]
    for d in data:
        print(solution(d))