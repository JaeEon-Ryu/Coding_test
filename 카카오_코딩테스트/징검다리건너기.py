# 시간초과가 났음
# 코드 리팩도링 필요

def solution(stones, k):
    answer = 0
    crossingable = True
    stones.insert(0,'start')
    stones.append('end')

    while crossingable:
        position = 0
        crossing = True

        while crossing:
            position += 1

            if stones[position] == 'end':
                answer += 1
                break
            elif stones[position] < 1:

                release = 0
                for bonus in range(1,k):
                    position += 1
                    crossingable = False

                    if stones[position] == 'end':
                        crossingable = True
                        crossing = False
                        answer += 1
                        break

                    if stones[position] > 0:
                        stones[position] -= 1
                        crossingable = True
                        break
                    else :
                        release += 1

                if release+1 == k :
                    break


            else:
                stones[position] -= 1

    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones,k))
