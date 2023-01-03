import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

import sys
sys.setrecursionlimit(10**6)
num_list = []
while True:
    try:
        num = int(input())
        num_list.append(num)
    except:
        break

def postOrder(start, size):
	if size <= 0:
		return
	root = num_list[start]
	leftSize = size - 1
	for i in range(start + 1, start + size):
		if num_list[start] < num_list[i]:
			leftSize = i - start - 1
			break
	rightSize = size - leftSize - 1
	postOrder(start + 1, leftSize)
	postOrder(start + leftSize + 1,rightSize)
	print(root)
	
postOrder(0, len(num_list))