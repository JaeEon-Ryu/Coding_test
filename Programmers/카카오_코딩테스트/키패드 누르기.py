def solution(numbers, hand):
    answer = ''
    side_l = [1,4,7,10]
    side_m = [2,5,8,0]
    side_r = [3,6,9,12]

    location_of_thumb = dict()
    location_of_thumb['l'] = '03' # 0행3열에 위치
    location_of_thumb['r'] = '23' # 2행3열에 위치

    for num in numbers:
        if num in side_l : # 왼쪽 키패드
            answer += 'L'
            location_of_thumb['l'] = '0' + str(side_l.index(num))
            #add_answer('l','0',str(side_l.index(num)))
        elif num in side_r : # 오른쪽 키패드
            answer += 'R'
            location_of_thumb['r'] = '2' + str(side_r.index(num))
        else: # 중앙에 있는 번호일 경우
            index_l = location_of_thumb['l']
            index_r = location_of_thumb['r']
            distance_l = abs(int(index_l[0]) - 1) + abs(int(index_l[1]) - side_m.index(num))
            distance_r = abs(int(index_r[0]) - 1) + abs(int(index_r[1]) - side_m.index(num))
            print(distance_l,'   ',distance_r)
            if distance_l == distance_r:
                if hand == 'left':
                    answer += 'L'
                    location_of_thumb['l'] = '1' + str(side_m.index(num))
                else:
                    answer += 'R'
                    location_of_thumb['r'] = '1' + str(side_m.index(num))
            else:
                if distance_l < distance_r:
                    answer += 'L'
                    location_of_thumb['l'] = '1' + str(side_m.index(num))
                else:
                    answer += 'R'
                    location_of_thumb['r'] = '1' + str(side_m.index(num))

    return answer

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers,hand))