def solution(source):
    answer = ''

    while True:
        result = []
        dest = []
        for i in source:
            if i not in result:
                result.append(i)
            else:
                dest.append(i)
        result.sort()
        for j in result:
            answer += j

        if len(dest) == 0:
            break
        else:
            source = ''.join(dest)

    return answer

a = "execute"
b = "cucumber"
c = "bbaabd"
print(solution(c))

