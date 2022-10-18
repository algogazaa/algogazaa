# n, m = list(map(int, input().split()))
# num = list(map(int, input().split()))
# divide = sum(num) // m
# summ = 0
# result = []
# num_list = []
# s_list = []
# for i in num:
#     if abs(divide-summ) >= abs(divide-summ-i):
#         summ += i
#         s_list.append(i)
#     else:
#         result.append(summ)
#         num_list.append(s_list)
#         s_list = []
#         summ = i
#         s_list.append(i)
# num_list.append(s_list)
# result.append(summ)
#
# while len(result) != m:
#     index = result.index(max(result))
#     if len(num_list[index]) != 1:
#         result[index] = num_list[index][0]
#         a = sum(num_list[index][1:])
#         result.append(a)
#     else:
#         break
#
# print(max(result))


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
data = list(map(int, input().split()))

num = sum(data)

start = 0   # num // 3
end = 10000000000
result = num

while start <= end:
    # mid 는 블루레이 크기
    mid = (start+end) // 2
    if mid < max(data):
        start = mid + 1
        continue

    cnt, tmp = 1, 0

    for i in range(len(data)):

        if tmp + data[i] <= mid:
            tmp += data[i]

        else:
            tmp = data[i]
            cnt += 1

    if cnt <= m:
        end = mid - 1
        result = min(result, mid)
    else:
        start = mid + 1

print(result)