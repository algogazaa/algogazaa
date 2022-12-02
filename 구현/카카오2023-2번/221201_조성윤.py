def solution(cap,n,deliveries, pickups):
    result = 0
    while deliveries and pickups:
        deliveryDist = len(deliveries) if len(deliveries) >= len(pickups) else len(pickups)
        deliveryCnt = 0
        pickupCnt = 0
        
        while deliveries and deliveryCnt <= cap:
            deliveryNum = deliveries.pop()
            deliveryCnt += deliveryNum
        
            if deliveryCnt > cap:
                deliveries.append(deliveryNum)
                break
            
        while pickups and pickupCnt <= cap:
            pickupNum = pickups.pop()
            pickupCnt += pickupNum
        
            if pickupCnt > cap:
                pickups.append(pickupNum)
                break
        
        result += 2 * deliveryDist
                
    return result

if __name__ == "__main__":
    cap = [4,2]
    n = [5,7]
    deliveries = [[1,0,3,1,2],[1,0,2,0,1,0,2]]
    pickups = [[0,3,0,4,0],[0,2,0,1,0,2,0]]
    
    for a,b,c,d in zip(cap,n,deliveries,pickups):
        print(solution(a,b,c,d))