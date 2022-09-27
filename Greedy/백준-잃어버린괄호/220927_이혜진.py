arr=input().split('-') #'-'기준으로 자른 배열 ['12+003', '001+2', '1']

num=0
first=arr[0].split('+') #['12','003']
for n in first:
    num+=int(n)

arr.pop(0)

#나머지 ['001+2', '1']
for a in arr:
    others=a.split('+')
    for m in others:
        num-=int(m) 

print(num)
