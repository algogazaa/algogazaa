n, m = input().split()
count = 0

if len(n) != len(m):
    print(0)
else:
    n_list = list(n)
    m_list = list(m)

    for i in range(len(n_list)):
        if n_list[i] == m_list[i] and m_list[i] == '8' and n_list[i] == '8':
            count += 1
        else:
            break
    print(count)


## ??!?!?!?!?