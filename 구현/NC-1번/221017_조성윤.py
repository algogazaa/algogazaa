from collections import deque
def solution(source):
    source = deque(list(source))
    dest = []
    finalDest = ''
    while source:
        dest = []
        for i in range(len(source)):
            tempStr = source.popleft()
            if tempStr not in dest:
                dest.append(tempStr)
            else:
                source.append(tempStr)
        dest.sort()
        finalDest += ''.join(dest)
    
    return finalDest
            
            
if __name__ == "__main__":
    source = ["execute", "cucumber","bbaabd"]
    for s in source:
        print(solution(s))