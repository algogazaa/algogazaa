#
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
tree = list(map(int, input().split()))
perfectTree = [[] for _ in range(n)]
def dfs(start, end, depth):
    # 종료 조건
    if start > end or depth > n - 1:
        return
    # root값 트리에 맞는 depth 레벨에 넣기
    rootIdx = (start + end) // 2
    root = tree[rootIdx]
    perfectTree[depth].append(root)
    # 왼쪽 노드 순회
    dfs(start,rootIdx - 1,depth + 1)
    # 오른쪽 노드 순회
    dfs(rootIdx + 1,end,depth + 1)

dfs(0,len(tree)-1,0)
for level in perfectTree:
    for i in level:
        print(i, end = " ")
    print()