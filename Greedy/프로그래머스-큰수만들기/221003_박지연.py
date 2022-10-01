def solution(number, k):
    number_list = list(number)
    cut_list = number_list[:k+1]

    max_first = max(cut_list)
    max_index = cut_list.index(max_first)

    a = number_list[max_index:]
    i = 1

    while len(a) != len(number) - k:
        if i == len(a)-1:
            break
        if a[i] < a[i+1]:
            a = a[:i] + a[i+1:]

        i += 1

    if len(a) > len(number) - k:
        a = a[:len(number)-k]

    return ''.join(a)

a = "4177252841"
b = "654321"
c = "1234567"
print(solution(c, 4))