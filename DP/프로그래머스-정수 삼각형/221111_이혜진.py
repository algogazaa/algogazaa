def solution(triangle):
    n=len(triangle)
    d=[]
    for i in range(1,n+1):
        d.append([0]*i)
    
    d[0][0]=triangle[0][0]
    for i in range(1,n):
        for j in range(0,i+1):
            #외곽 처리
            if j==0:
                d[i][j]=d[i-1][j]+triangle[i][j]
            elif j==i:
                d[i][j]=d[i-1][j-1]+triangle[i][j]
            else:
                d[i][j]=max(d[i-1][j-1],d[i-1][j])+triangle[i][j]
            
    return max(d[n-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
