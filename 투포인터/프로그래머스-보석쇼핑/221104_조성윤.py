def solution(gems):
	kinds = set(gems)
	shortest = len(gems) - 1
	start = 0
	end = 0
	cnt_gems = {gems[0]:1}
	result = [1,len(gems)]

	while start < len(gems) and end < len(gems):
		if len(cnt_gems) == len(kinds): # 보석 종류를 다 모았다면
			cnt_gems[gems[start]] -= 1
			if cnt_gems[gems[start]] == 0:
				del cnt_gems[gems[start]]
				if shortest > end - start:
					shortest = end - start
					result = [start + 1, end + 1]

			start += 1
			if start == len(gems):
				break
		else: # 모으지 못했다면
			end += 1
			if end == len(gems):
				break		
			if gems[end] not in cnt_gems:
				cnt_gems[gems[end]] = 1
			else:
				cnt_gems[gems[end]] += 1
	
	return result