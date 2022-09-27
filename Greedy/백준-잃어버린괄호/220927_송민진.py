calc_str = input()
operation_list = []
answer = 0

for letter in calc_str:
    if letter == '+' or letter == '-':
        operation_list.append(letter)

calc_str = calc_str.replace('+', '-')
num_list = list(map(int, calc_str.split('-')))

answer += num_list[0]
num_list.remove(num_list[0])

for i in range(len(operation_list)):
    if i != 0 and operation_list[i] == '+' and operation_list[i-1] == '-':
        operation_list[i] = '-'
    if num_list:
        if operation_list[i] == '+':
            answer += num_list[0]
            num_list.remove(num_list[0])
        else:
            answer -= num_list[0]
            num_list.remove(num_list[0])

print(answer)
