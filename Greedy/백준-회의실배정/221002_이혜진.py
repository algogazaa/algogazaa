n=int(input())
s=[]
for i in range(n):
    first, second=map(int,input().split())
    s.append([first,second])
s=sorted(s,key=lambda x:x[0])
s=sorted(s,key=lambda x:x[1]) #중요한 마지막시간 비교는 제일 끝에
cnt=0
last=0
for i,j in s:
    if i>=last: #2차원 배열에서 요소[1]의 last와 요소[2]의 first를 비교
        cnt+=1
        last=j
print(cnt)
