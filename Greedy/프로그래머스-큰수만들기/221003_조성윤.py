def solution(number, k):
    stack = []
    
    for num in number:
        if not stack:
            stack.append(num)
            continue
        
        while k != 0 and stack[-1] < num:
            stack.pop()
            k -= 1
            if not stack:
                break

        if k == 0:
            stack.append(num)
            continue

        stack.append(num)

    stack = stack[:-k] if k > 0 else stack
    return ''.join(stack)