number = "4177252841"
k = 4

def solution1(number, k):
    answer = ''
    
    while k > 0:
        max_num_index = number.index(max(number[:k+1])) + 1
        answer += number[max_num_index-1]
        number = number[max_num_index:]
        k -= max_num_index - 1
        if len(number) == k:
            return answer
        
    answer += number
    
    return answer

### 시간 초과


import heapq

def solution2(number, k):
    answer = ''
    
    while k > 0:
        q = []
        for i in range(k+1):
            heapq.heappush(q, -int(number[i]))
        max_num = -heapq.heappop(q)
        max_num_index =  number.index(str(max_num))
        answer += str(max_num)
        number = number[max_num_index + 1:]
        k -= max_num_index
        if len(number) == k:
            return answer

    answer += number
    
    return answer

### 시간 초과


def solution3(number, k):
    answer = ''
    
    while k > 0:
        max_num = '0'
        for x in range(k+1):
            if max_num < number[x]:
                max_num = number[x]
        answer += max_num
        k -= number.index(max_num)
        number = number[number.index(max_num) + 1:]
        if len(number) == k:
            return answer
        
    for _ in number:
        answer += _
        
    return answer

# 10번 시간 초과


def solution(number, k):
    answer = ''
    
    while k > 0:
        max_num = '0'
        for x in range(k+1):
            if max_num == '9':
                break
            elif max_num < number[x]:
                max_num = number[x]
        answer += max_num
        k -= number.index(max_num)
        number = number[number.index(max_num) + 1:]
        if len(number) == k:
            return answer
        
    for _ in number:
        answer += _
        
    return answer

print(solution(number,k))
