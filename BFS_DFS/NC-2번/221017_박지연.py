def solution(music):
    answer = 0
    cnt = 1
    white = [1, 3, 5, 7, 8, 10, 12]
    index = [0, 0, 0, 1, 1, 2, 2, 3, 4, 3, 5, 4, 6]

    for i in music:

        if cnt not in white:
            if cnt > i:
                cnt -= 1
            else:
                cnt += 1
            answer += 1

        if cnt < i:
            if i in white:
                c_index = index[cnt]
                i_index = index[i]
                answer += i_index - c_index
            else:
                c_index = index[cnt]
                i_index = index[i-1]
                answer += i_index - c_index + 1
        elif cnt == i:
            continue
        else:
            if i in white:
                c_index = index[cnt]
                i_index = index[i]
                answer += c_index - i_index
            else:
                c_index = index[cnt]
                i_index = index[i+1]
                answer += c_index - i_index + 1
        cnt = i

    return answer

a = [10, 9, 4, 5, 12] #15
b = [6, 4, 2, 11] #13
print(solution(b))