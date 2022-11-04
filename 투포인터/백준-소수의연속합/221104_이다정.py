N = int(input())

def prime_list(n):
  a = [True] * (n+1)
  m = int(n ** 0.5)
  for i in range(2, m+1):
    if a[i] == True:
      for j in range(i+i, n+1, i):
        a[j] = False
  return [i for i in range(2, n+1) if a[i] == True]

pl = prime_list(N)
end = 0
sum_part = 0
cnt = 0

for start in range(len(pl)):
  while sum_part < N and end < len(pl):
    sum_part += pl[end]
    end += 1

  if sum_part == N:
    cnt += 1

  sum_part -= pl[start]
  
print(cnt)
