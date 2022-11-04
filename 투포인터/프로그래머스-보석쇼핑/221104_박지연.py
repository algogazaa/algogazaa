def solution(gems):
    answer = [0, 0]
    min_length = len(gems)
    type = 0
    gem_type = []

    for i in gems:
        if i not in gem_type:
            type += 1
            gem_type.append(i)

    end, cnt = 0, 0
    gem_type = {}
    for start in range(len(gems)):
        while cnt < type and end < len(gems):
            if gems[end] not in gem_type:
                gem_type[gems[end]] = 1
                cnt += 1
            else:
                gem_type[gems[end]] += 1
            end += 1

        if cnt == type and end-start-1 < min_length:
            answer[0] = start + 1
            answer[1] = end
            min_length = end-start-1

        if gem_type[gems[start]] == 1:
            cnt -= 1
            del gem_type[gems[start]]
        else:
            gem_type[gems[start]] -= 1

    return answer


print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))