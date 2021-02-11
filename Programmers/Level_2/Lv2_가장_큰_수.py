#정수를 이어붙여 만들 수있는 가장 큰 수?

# 1.모든 수를 일의자리로 변경(나머지, 나누기 이용)
# 조건.중복된 수가 있는가?
#   yes:
#     중복된 수들 중 ~
#   no:
#     그 수를 리스트에서 빼서 문자화 하여 answer에 저장
#
# 1. 최대값을 찾는다.
# 2. 최대값 중에 중복된 값이 있는지 찾아본다.
# 3.중복된 값이 있다면 다음 자리수까지 살펴들어가며 비교
# 4.중복된 값이 없다면 answer에 덧붙인다.

# def solution(numbers):
#     answer = ''
#     DigitList = numbers[:]
#
#     for i in range(len(numbers)):  # 자리수 1자리로
#         find_NOD = str(DigitList[i])  # Number Of Digits
#         DigitList[i] = int(find_NOD[0])
#
#     for k in range(len(numbers)):
#         findMax = -5
#         maxIndex = 0
#         for i in range(len(numbers)):  # 큰 수 차례로 넣기
#             if findMax <= DigitList[i]:
#                 if findMax == DigitList[i]:
#                     turn = 0
#                     strF = str(numbers[maxIndex])
#                     strD = str(numbers[i])
#                     while turn != max(len(strF), len(strD)):
#                         if strF[-len(strF) + turn] < strD[-len(strD) + turn]:
#                             findMax = DigitList[i]
#                             maxIndex = i
#                             break
#                         turn += 1
#                 else:  # findMax < DigitList[i] 인 경우
#                     findMax = DigitList[i]
#                     maxIndex = i
#         answer += str(numbers[maxIndex])
#         DigitList[maxIndex] = -1
#
#     return answer

# -> 틀렸음.(시간복잡도가 너무 큼 )
# ( while 부분 인덱스 오류 - 너무 복잡함 )


# 2. 정수 리스트가 주어졌을 때
# 나올 수 있는 모든 경우의 수를 따져서 리스트에 저장
# 제일 큰 값을 뽑아낸다.
#
# numbers 크기가
# 1일 경우 -> 1
# 2일 경우 -> 2
# 3일 경우 -> 6
# 4일 경우 -> 24
#
# x y z k
#
# xyzk
# xykz
# xzyk
# xzky
# xkyz
# xkzy
#
# ---> numbers의 크기가 커질수록 시간복잡도가 너무 커짐(비효율)



# 3. 더 간단하게
#
# 6, 10, 2
# -> 6666 1010 2222
# 3 30 34 5 9
# -> 3333 3030 3434 5555 9999
# 121 12
# -> 121121 121212
# 12112 12121
#
# 311 1313
# -> 311311311311 1313131313131313
#
# 0 00 000 0000
# 12자리.


def solution(numbers):
    if sum(numbers) == 0: return '0'

    answer = ''
    numbers = [str(i) for i in numbers]
    numbers.sort(key=lambda x: x * 3, reverse=True)
    for i in numbers: answer += i

    return answer


# 정답