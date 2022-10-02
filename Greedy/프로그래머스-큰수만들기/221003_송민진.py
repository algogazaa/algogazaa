def solution(number, k):
    answer = []
    remove_num = k

    for num in number:
        
        if len(answer) == 0:
            answer.append(num)
            
        elif answer[-1] < num and k > 0:
            answer.pop()
            k -= 1
            answer.append(num)

            while len(answer) > 1:
                if answer[-2] < num and k > 0:
                    answer.pop(-2)
                    k -= 1
                else:
                    break
        
        else:
            answer.append(num)

    answer = "".join(answer)

    if len(answer) != len(number) - remove_num:
        answer = answer[:-remove_num]

    return answer
