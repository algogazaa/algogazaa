N = int(input())
vote_list = [int(input()) for _ in range(N)]
answer = 0

if N > 1:
    while max(vote_list[1:]) == max(vote_list):
        vote_list[vote_list[1:].index(max(vote_list))+1] -= 1
        vote_list[0] += 1
        answer += 1

print(answer)
