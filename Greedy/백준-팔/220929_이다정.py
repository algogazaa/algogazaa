L, R = input().split(" ")
cnt = 0

if len(L) == len(R):
    for i in range(len(L)):
        if L[i] == R[i] == '8':
            cnt += 1
        elif L[i] == R[i]:
            continue
        else:
            break

print(cnt)
