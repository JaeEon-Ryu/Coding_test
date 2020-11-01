def solution(k, room_number):
    result = []
    room_dict = dict()

    for number in room_number:
        visited = [number]

        while True:
            if room_dict.get(number) == None:
                result.append(number)
                break
            else:
                number = room_dict[number]
                visited.append(number)

        for _ in visited:
            room_dict[_] = number + 1

    return result



# def solution(k, room_number):
#     result = []
#     room_dict = dict()
#
#     for number in room_number:
#
#         while True:
#
#             if room_dict.get(number) == None:
#                 room_dict[number] = number + 1
#                 result.append(number)
#                 break
#             else:
#                 number = room_dict[number]
#
#
#     return result


''' 정확성은 만점 but 효율성 0 점 
def solution(k, room_number):
    result = []

    for number in room_number:
        if number in result:
            sorted(result)
            number+=1

            while number in result:
                number += 1
            result.append(number)

        else:
            result.append(number)

    return result
'''

k = 10
room_number = [1, 3, 4, 1, 3, 1]
print(solution(k, room_number))