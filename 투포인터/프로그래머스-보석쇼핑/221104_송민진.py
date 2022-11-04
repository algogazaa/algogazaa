def solution(gems):
    answer = []
    total_types_cnt = len(set(gems))
    cart_types_cnt = 0
    cart = {}
    min_length = float('inf')

    right = 0
    for left in range(len(gems)):
        while left <= right < len(gems):

            if cart_types_cnt == total_types_cnt:
                break

            else:
                if gems[right] in cart:
                    cart[gems[right]] += 1
                else:
                    cart[gems[right]] = 1
                    cart_types_cnt += 1
                right += 1

        if cart_types_cnt == total_types_cnt:
            if min_length > right - left:
                min_length = right - left
                answer = [left + 1, right]

        if gems[left] in cart:
            if cart[gems[left]] > 1:
                cart[gems[left]] -= 1
            elif cart[gems[left]] == 1:
                del cart[gems[left]]
                cart_types_cnt -= 1

    return answer