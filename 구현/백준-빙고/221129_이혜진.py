bingo=dict()
numbers=[]
call=[]

for i in range(5):
    numbers=list(map(int,input().split()))
    for j in range(5):
        bingo[numbers[j]]=(i,j) #숫자 : (좌표)

for _ in range(5):
    call.extend(list(map(int,input().split())))

check={'a0':0,'a1':0,'a2':0,'a3':0,'a4':0,'b0':0,'b1':0,'b2':0,'b3':0,'b4':0,'c1':0,'c2':0}

def check_num(num):
    x,y=bingo[num]
    check['a'+str(x)]+=1
    check['b'+str(y)]+=1
    if(x==y): #대각선1
        check['c1']+=1
    if(4-x==y):#대각선2
        check['c2']+=1

def count_val(dic,val):
    cnt=0
    for key, value in dic.items():
        if val == value:
            cnt+=1
    return cnt

result=0
for num in call:
    check_num(num)
    result+=1
    if count_val(check,5)>2:
        print(result)
        break
