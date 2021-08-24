def solution(scores):
    answer = ''

    # 점수 계산기
    def get_degree(s):
        if s >= 90:
            return 'A'
        elif s >= 80:
            return 'B'
        elif s >= 70:
            return 'C'
        elif s >= 50:
            return 'D'
        else:
            return 'F'

    # 행렬의 원소 각각 보기
    N = len(scores)
    for j in range(N):

        max_s, min_s = -1, 101
        max_cnt, min_cnt = 0, 0
        sum_s = 0
        for i in range(N):

            s = scores[i][j] # 현재 원소값
            sum_s += s # 값 누적

            # 최대값, 개수 갱신
            if s > max_s:
                max_s = s
                max_cnt = 1
            elif s == max_s:
                max_cnt += 1

            # 최소값, 개수 갱신
            if s < min_s:
                min_s = s
                min_cnt = 1
            elif s == min_s:
                min_cnt += 1

        self_s = scores[j][j] # 자기 자신의 점수
        avg_s = 0

        # 유일한 최고점, 최저점일 때 계산
        if (self_s == max_s and max_cnt == 1) or (self_s == min_s and min_cnt == 1):
            avg_s = (sum_s - self_s) / (N - 1)
        else:
            avg_s = sum_s / N

        answer += get_degree(avg_s)

    return answer


'''
reference : aeanst
행렬을 뒤집고 풀이하면 더욱 간단하게 해결가능 함 ( 배울점 ) 

def solution(scores) :

    avgs=[]

    score=[ [i[j] for i in scores] for j in range(len(scores))]

    for idx,i in enumerate(score) :

        avg=sum(i) ; length=len(i)

        if i[idx] == max(i) or i[idx] == min(i) :

            if i.count(i[idx]) == 1 :

                avg-=i[idx] ; length-=1

        avgs.append(avg/length)

    return "".join([ avg>=90 and "A" or avg>=80 and "B" or avg>=70 and "C" or avg>=50 and "D" or "F" for avg in avgs ])
'''