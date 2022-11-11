def solution(triangle):
    sum_list = []
    sum_list.append([triangle[0][0]])

    if len(triangle) >= 2:
        sum_list.append([sum_list[0][0] + triangle[1][0], sum_list[0][0] + triangle[1][1]])

    for i in range(2, len(triangle)):
        cnt = 0
        sum_list2 = []

        for j in range(len(triangle[i])):
            if j == 0 or j == len(triangle[i]) -1:
                k = sum_list[i-1][cnt] + triangle[i][j]
                sum_list2.append(k)
            else:
                k = max(sum_list[i-1][cnt] + triangle[i][j], sum_list[i-1][cnt+1] + triangle[i][j])
                sum_list2.append(k)
                cnt += 1
        sum_list.append(sum_list2)

    return max(sum_list[len(sum_list)-1])

# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
