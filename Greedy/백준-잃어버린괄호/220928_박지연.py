n = input()
n_list = n.split('-')
p_num = 0

if '+' in n_list[0]:
    p_list = n_list[0].split('+')
    for i in p_list:
        p_num += int(i)
else:
    p_num += int(n_list[0])

for j in range(1, len(n_list)):
    if '+' in n_list[j]:
        m_list = n_list[j].split('+')
        for k in m_list:
            p_num -= int(k)
    else:
        p_num -= int(n_list[j])

print(p_num)


