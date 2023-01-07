#
import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for _ in range(n + 1)]
info = [[],[0,0]]
for i in range(n - 1):
    animal, amount, connection = input().split()
    tree[int(connection)].append(i + 2)
    info.append([animal, int(amount)])

def dfs(parent):
    result = 0
    # 부모의 자식 노드들 탐색
    for child in tree[parent]:
        result += dfs(child)
    # 늑대일때
    if info[parent][0] == 'W':
        result -= info[parent][1]
        if result < 0:
            return 0
    # 양일 때
    else:
        result += info[parent][1]
    
    return result

print(dfs(1))