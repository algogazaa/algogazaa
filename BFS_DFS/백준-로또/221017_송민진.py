def dfs(depth, idx):
    if depth == 6:
        print(*result_list)
        return

    for i in range(idx, k):
        result_list.append(testcase[i])
        dfs(depth+1, i+1)
        result_list.pop()

while True:
    result_list = []
    testcase = list(map(int, input().split()))
    k = testcase.pop(0)
    dfs(0, 0)
    if k == 0:
        exit()
    print()
