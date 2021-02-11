# 장르별 - 많이 재생된 노래를 두개씩 - 고유 번호 구분
#
# genres & plays  -> ditionary화.
#
# 1. 장르 노래 합으로 정렬
# 2. 장르 안에서는 재생순 정렬
# 2-2. 재생 횟수가 같다면 고유번호가 낮은순
#
# g리스트
# [c,      p    , c  ,   c,     p]
# p리스트
# [500, 600, 150, 800, 2500]
# answer리스트
# [0,     1,       2,     3,     4]
#
# 딕셔너리화 -> 인덱스 번호를 활용해야하므로
# 쓰지 않음. xxxxxxxxxxx-> 써야 함.
# 장르별 합을 구할 때 써야한다.
#
#
# 1. 장르를 재생순으로 정렬한다
# 2. 정렬된 장르 리스트를 기준으로
# 새로운 리스트에 재생목록들을 담는다
# 3. 재생목록에서 최대값, 그다음 최대값을 뽑아서
# answer에 추가한다.


def solution(genres, plays):
    import operator
    answer = []
    dict_gp = {} # dictionary (genres, plays)

    # for search the most plays
    for i,g in enumerate(genres):
        if g in dict_gp :
            dict_gp[g] += plays[i]
        else :
            dict_gp[g] = plays[i]
    dict_gp = sorted(dict_gp.items(),key=operator.itemgetter(1),reverse=True)

    # find answer
    for i in range(len(dict_gp)): # find plays that fit genres
        play_list = []
        number_list = []
        for n,g in enumerate(genres): # make list by genre
            if dict_gp[i][0] == g:
                play_list.append([plays[n]])
                number_list.append(n)

        for num in range(len(play_list)): # Add 2 of the plays
            if num == 2 : break
            index = play_list.index(max(play_list))
            answer.append(number_list[index])
            play_list.pop(index)
            number_list.pop(index)

    return answer


# ---------------------------------------------------------

# 다른사람이 쓴 코드 분석
def solution(genres, plays):
    answer = []
    d = {e:[] for e in set(genres)}
    for e in zip(genres, plays, range(len(plays))):
        d[e[0]].append([e[1] , e[2]])
    genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
    for g in genreSort:
        temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
        answer += temp[:min(len(temp),2)]
    return answer


# lambda 안의 lambda :
# x는 list(d.keys())의 원소를 의미하고,
# map 함수 안에 있는 lambda의 y는 d[x]의 원소
# 따라서 x(genre)를 받아서
# d[x] (dictionary d의 해당 장르에 속한 음악 고유번호
# 와 play된 수 list)에서 play된 수만 추출하고,
# 그 값들을 모두 합한 값을 key로 sorted를 하게 되는 것


# -----------------------------------------------------

import operator
from collections import defaultdict

class Music:
    def __init__(self, id, g, p):
        self.id = id
        self.g = g
        self.p = p

def solution(genres, plays):
    db = []
    g_db = defaultdict(int)
    for i in range(len(genres)):
        db.append(Music(i,genres[i],plays[i]))
        g_db[genres[i]] += plays[i]
    db.sort(key=operator.attrgetter("id"))
    db.sort(key=operator.attrgetter("p"),reverse=True)

    g_db = sorted(g_db.items(),key=operator.itemgetter(1), reverse=True)

    result = []
    for g in g_db:
        idx = 0
        cnt = 0
        while cnt <2:
            if idx >= len(db):
                break
            if db[idx].g == g[0]:
                result.append(db[idx].id)
                cnt += 1
            idx += 1
    return result