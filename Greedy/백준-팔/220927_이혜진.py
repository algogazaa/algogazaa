L,R=map(str,input().split())

cnt=0
if len(L)!=len(R): #자리수가 다름 (무조건 0)
    cnt=0
else: #자리수가 같음
    for i in range(len(L)):
        if L[i]==R[i] and L[i]=='8': 
            cnt+=1
        elif L[i]==R[i] and L[i]!='8':
            continue
        else:
            break

print(cnt)



#1차시도 (시간초과)

# L,R=map(int,input().split())
# cnt=[]
# for i in range(L,R+1):
#     cnt.append(str(i).count('8'))

# print(min(cnt))

#2차시도 (시간초과)
# L,R=map(int,input().split())
# cnt=str(L).count('8')
# for i in range(L,R+1):

#     #8이 없는 경우
#     if '8' not in str(i):
#         cnt=0
#         continue
#     #8이 있으면 min갱신
#     else:
#         cnt=min(cnt,str(i).count('8'))

# print(cnt)
