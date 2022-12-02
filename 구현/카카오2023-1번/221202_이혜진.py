def solution(today, terms, privacies):
    answer=[]
    #약정 정의
    dic={}
    for t in terms:
        a,b=map(str,t.split())
        dic[a]=b
    
    #오늘날짜
    ty,tm,td=map(int,today.split('.'))

    idx=0
    for p in privacies:
        idx+=1
        term=int(dic[p[-1]])
        p = p[:-1]

        y,m,d=map(int,p.split('.'))
        m+=term
        while m>12:
            y+=1
            m-=12
            if m<=12:
                break

        if ty>y:
            answer.append(idx)
        elif ty==y and tm>m:
            answer.append(idx)
        elif ty==y and tm==m and td>=d:
            answer.append(idx)
        
    return answer
