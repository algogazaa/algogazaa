import sys
input = sys.stdin.readline

K = int(input())
nodes = list(map(int, input().split()))
tree = [[] for _ in range(K)]


def make_tree(nodes, depth):
    center = len(nodes) // 2
    tree[depth].append(nodes[center])
    if len(nodes) == 1:
        return
    make_tree(nodes[:center], depth+1)
    make_tree(nodes[center+1:], depth+1)


make_tree(nodes, 0)
for t in tree:
    print(*t)
