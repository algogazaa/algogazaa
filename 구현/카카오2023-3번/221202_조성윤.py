import sys
sys.setrecursionlimit(10**6)
def solution(users, emoticons):
    global result
    result = [0,0]
    dfs([],emoticons, users)
    return result

def dfs(totalRateList,emoticons,users):
    global result
    discountRate = [10,20,30,40]
    if len(totalRateList) == len(emoticons):
        subscribe = 0
        totalProfit = 0
        tempUsers = [0] * len(users)
        for i in range(len(totalRateList)):
            discountedMoney = emoticons[i] * (100 - totalRateList[i]) // 100
            for j in range(len(users)):
                if users[j][0] <= totalRateList[i]:
                    tempUsers[i] += discountedMoney
        
        for i in range(len(users)):
            if users[i][1] <= tempUsers[i]:
                subscribe += 1
            else:
                totalProfit += tempUsers[i]
        
        if result < [subscribe, totalProfit]:
            result = [subscribe, totalProfit]
        return
            
        
    for rate in discountRate:
        totalRateList.append(rate)
        dfs(totalRateList, emoticons, users)
        totalRateList.pop()

    
if __name__ == "__main__":
    users = [[[40,10000],[25,10000]],[[40,2900],[23,10000],[11,5200],[5,5900],[40,3100],[27,9200],[32,6900]]]
    emoticons = [[7000,9000],[1300,1500,1600,4900]]
    for a, b in zip(users, emoticons):
        print(solution(a,b))