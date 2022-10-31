import sys
input = sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
target=int(input())

def b(arr,target,start,end):
    if sum(arr)<=target:
        return max(arr)

    while start<=end:
        mid=(start+end)//2
        total=0
        for i in arr:
            if i<=mid:
                total+=i
            else:
                total+=mid
        
        if total==target:
            #result=mid #시간초과 (start,end값이 안바껴서 무한루트)
            return mid
        elif total<target:
            start=mid+1
            result=mid
        else:
            end=mid-1

    return result


print(b(arr,target,0,max(arr)))
