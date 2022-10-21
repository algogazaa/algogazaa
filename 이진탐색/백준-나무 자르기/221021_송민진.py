n, m = map(int, input().split())
heights = list(map(int, input().split()))


def binary_search(arr, start, end):
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0

        for x in arr:
            if x > mid:
                total += x - mid

        if total < m:
            end = mid - 1

        else:
            result = mid
            start = mid + 1

    return result


answer = binary_search(heights, 0, max(heights))
print(answer)
