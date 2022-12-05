import sys

def solution(numbers):
    global possible
    result = []
    for n in numbers:
        targetNum = bin(n)[2:]
        i = 0
        while 2 ** i < len(targetNum):
            i += 1
        targetNum = list('0' * (2 ** i - 1 - len(targetNum)) + targetNum)
        possible = 1
        dfsTree(targetNum,len(targetNum),1,i)
        result.append(possible)
    return result

def dfsTree(target,root,depth,height):
    global possible
    root = root // 2
    if depth == height:
        return
    if depth != height and target[root] == '0':
        possible = 0
        return
    left = root - 1
    right = root + 1
    dfsTree(target, left, depth + 1, height)
    dfsTree(target, right, depth + 1, height)
    return
    
if __name__ == "__main__":
    numbers = [[111,5],[63,111,95]]
    for n in numbers:
        print(solution(n))