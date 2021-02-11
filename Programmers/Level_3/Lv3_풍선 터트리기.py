def solution(a):
    answer = 2 # 길이가 2 이하일 경우를 대비하여
    left,right = a[0],a[-1]

    for idx in range(1,len(a)-1):
        if left > a[idx]:
            answer += 1
            left = a[idx]

    for idx in range(len(a)-1,1,-1):
        if right > a[idx]:
            answer += 1
            right = a[idx]

    if left != right:
        return answer
    else:
        return answer-1

# n세제곱의 코드 -> 알고리즘 다시 짜기
# def solution(a):
#     answer = 0
#     point = 0
#     chance = 1
#
#     while point != len(a):
#
#         b = a[:]
#
#         while len(b) > 3:
#
#             for index in range(len(b)-1):
#
#                 try:
#                     max_value = max(b[index],b[index+1])
#                     max_index = b.index(max_value)
#                 except :
#                     break
#
#                 if max_value != a[point]:
#                     b.pop(max_index)
#
#         if b.index(a[point]) == 0 or b.index(a[point]) == 2:
#             answer += 1
#         else:
#             if max(b) != a[point]:
#                 answer += 1
#
#         point+=1
#
#     return answer

a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
print(solution(a))