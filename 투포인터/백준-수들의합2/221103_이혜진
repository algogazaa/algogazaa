n,m=map(int,input().split())
arr=list(map(int,input().split()))
start_idx=0
i=0
tmp=0
cnt=0
while(start_idx+i<len(arr)):
    if(tmp<m):
        tmp+=arr[start_idx+i]
        i+=1
    #m에 도달하면
    if(tmp==m):
        start_idx+=1
        i=0
        tmp=0
        cnt+=1
    #m에 도달하지 못하고 값만 커지면 -> 실패
    if(tmp>m):
        start_idx+=1
        i=0
        tmp=0
print(cnt)        
