# [3,0,6,1,5]
# -> 논문 n편 중, h번 이상 인용된 논문 h편 이상, 나머지 논문이 h번 이하 인용되었다면,  h가 이 과학자의 H-Index(답)
# => 이 과학자가 발표한 논문의 수는 5편, 그중 3편의 논문은 3회 이상 인용. 나머지 2편의 논문은 3회 이하 인용
# 때문에 이 과학자의 H-Index는 3

# [find _ solution]
# [3,0,6,1,5] -> [0,1,3,5,6] : 답 -> 3
# 중간 인덱스를 찾는?
# [0,1,1,5,7,9] : 답 -> 3

def solution(citations):
    sortedC = sorted(citations,reverse=True)
    i,h = 0,0
    while i<len(sortedC) and sortedC[i] > h:
        h+=1
        i+=1
    return h

