n, m = map(int, input().split())
lessons = list(map(int, input().split()))

right = sum(lessons)  # 레슨을 하나의 레코드에 다 담을 수 있을 때 레코드의 크기
left = max(lessons)  # 레코드가 가질 수 있는 가장 작은 크기

while left <= right:

    cnt = 0
    mid = (left + right) // 2
    sum_lesson = 0  # 한 레코드에 들어갈 레슨들의 합

    for i in range(n):
        if sum_lesson + lessons[i] > mid:
            cnt += 1
            sum_lesson = 0

        sum_lesson += lessons[i]

    else:
        if sum_lesson:
            cnt += 1

    if cnt <= m:
        right = mid - 1

    elif cnt > m:
        left = mid + 1

print(left)
