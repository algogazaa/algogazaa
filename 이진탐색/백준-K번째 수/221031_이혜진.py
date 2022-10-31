n=int(input())
k=int(input())


def b(k,n,start,end):
    while start<=end:
        mid=(start+end)//2
        sum=0
        for i in range(1,n+1):
            sum+=min(mid//i,n)
        
        if sum>=k:
            end=mid-1
            result=mid 
        else:
            start=mid+1
    
    return result

print(b(k,n,1,k))

# arr=[[0 for _ in range(n+1)] for _ in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         arr[i][j]=i*j

# brr=[0 for _ in range((n*1)*(n*1))]

