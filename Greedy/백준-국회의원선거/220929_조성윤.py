N = int(input())
a = []
cnt = 0
for _ in range(N):
	a.append(int(input()))

dasom = a[0]
if N != 1:
	b = a[1:]
	b.sort()
	while dasom <= b[-1]:
		b[-1] -= 1
		dasom += 1
		cnt += 1
		b.sort()

print(cnt)