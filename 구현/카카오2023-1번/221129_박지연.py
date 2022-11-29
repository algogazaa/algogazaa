def solution(today, terms, privacies):
    answer = []
    t_list = today.split('.')
    dic_term = {}

    for i in terms:
        j = i.split(" ")
        dic_term[j[0]] = j[1]

    for i in range(len(privacies)):
        p_day = privacies[i].split(" ")[0].split(".")
        p_type = privacies[i].split(" ")[1]

        p_day[2] = int(p_day[2]) - 1
        p_day[1] = int(p_day[1]) + int(dic_term[p_type])
        p_day[0] = int(p_day[0])

        if p_day[2] == 0:
            p_day[2] = 28
            p_day[1] -= 1
        while p_day[1] > 12:
            p_day[1] -= 12
            p_day[0] += 1

        if p_day[0] < int(t_list[0]):
            answer.append(i+1)
        elif p_day[0] == int(t_list[0]):
            if p_day[1] < int(t_list[1]):
                answer.append(i+1)
            elif p_day[1] == int(t_list[1]):
                if p_day[2] < int(t_list[2]):
                    answer.append(i+1)


    return answer



print(solution("2022.05.19", ["A 6", "B 12", "C 3"],
               ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"],
               ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))