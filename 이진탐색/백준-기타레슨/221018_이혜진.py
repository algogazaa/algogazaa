
def b(arr,start,end,m):
    result=10**9
    while start<=end:
        mid=(start+end)//2
        cnt=1
        tmp=0
        for le in arr:
            if tmp+le<=mid:
                tmp+=le
            else: #mid보다 크면
                cnt+=1
                tmp=le #tmp에 처음 들어가는 값
            if cnt>m:
                break
        
        if cnt>m: #많이 나눠진 것=mid가 작다=mid를 크게 만들어야한다
            start=mid+1
        else:
            end=mid-1
            if(mid>=max(arr)):
                result=min(result,mid)
    
    return result


if __name__ == "__main__":
    n,m=map(int,input().split())
    arr=list(map(int,input().split()))

    start=max(arr)
    end=sum(arr)
    print(b(arr,start,end,m))
