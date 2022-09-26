n=int(input())
dasom=int(input())
others=[int(input()) for _ in range(n-1)]

cnt=0
if n!=1:
    while dasom<=max(others):
        idx=others.index(max(others))
        others[idx]-=1
        dasom+=1
        cnt+=1

print(cnt)
