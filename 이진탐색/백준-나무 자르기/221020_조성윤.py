n, m = list(map(int,input().split())) # n과 m을 입력 받음

array = list(map(int,input().split())) # 나무의 높이가 주어짐

start = 0 # 시작지점
end = max(array) # 종결지점

result = 0
while(start<=end): # while 문 시작, start <= end 일 때 까지 실행
    total = 0
    mid = (start+end)//2

    for x in array:
        if x>mid: # 절단기 높이보다 높으면,
            total += x-mid

    if total < m: # total이 m보다 작다면, 더 절단기의 높이를 줄이는 방향으로,
        end = mid-1

    else:
        result = mid
        start = mid+1

print(result) # 결과 출력