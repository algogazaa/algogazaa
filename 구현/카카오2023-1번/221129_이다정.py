today1 = "2022.05.19"
terms1 = ["A 6", "B 12", "C 3"]
privacies1 = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]

today2 = "2020.01.01"
terms2 = ["Z 3", "D 5"]
privacies2 = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]


from datetime import datetime

def des_terms(today, term, privacies):
    result = []

    temp_date = list(map(int,today.split(".")))
    cal_today = (temp_date[0]-2000)*12*28 + temp_date[1]*28 + temp_date[2]

    terms = {}
    for _ in term:
        condition = _.split(" ")
        terms[condition[0]] = int(condition[1])

    for num, _ in enumerate(privacies):
        privacy = _.split(" ")
        date = list(map(int, privacy[0].split(".")))
        cal_expire = (date[0]-2000)*12*28 + (date[1]+terms[privacy[1]])*28 + date[2]
        # print(cal_expire, cal_today, num)
        if cal_expire <= cal_today:
            result.append(num+1)

    return result


print(des_terms(today2, terms2, privacies2))
