def solution(table, languages, preference):
    answer, max_score = '', 0

    for t in table:
        t = t.split()[::-1] # 언어에 대한 점수를 원활히 얻기 위해 역순 정렬

        score = 0
        for l, p in zip(languages, preference):
            if l not in t: # 언어가 해당 테이블에 없으면 pass
                continue

            score += (t.index(l) + 1) * p # 점수 계산

            if score > max_score:
                max_score = score
                answer = t[-1]
            elif score == max_score: # 점수가 동일할 경우 사전순 return
                answer = answer if answer < t[-1] else t[-1]

    return answer

