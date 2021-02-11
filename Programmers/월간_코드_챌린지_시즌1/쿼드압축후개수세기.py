global count_0
global count_1

count_0 = 0
count_1 = 0

def equal_in_number(arr):
    if len(set(sum(arr,[]))) == 1 :
        return True
    else :
        return False

def recursive_quarter(arr):
    global count_0
    global count_1
    list1,list2,list3,list4 = [],[],[],[]
    whole_list = []

    for i in range(len(arr)//2): # 상단 좌, 우

        list1_assist = []
        for j in range(len(arr) // 2):
            list1_assist.append(arr[i][j])
        list1.append(list1_assist)

        list2_assist = []
        for j in range(len(arr) // 2, len(arr)):
            list2_assist.append(arr[i][j])
        list2.append(list2_assist)

    for i in range(len(arr)//2, len(arr)): # 하단 좌, 우

        list3_assist = []
        for j in range(len(arr) // 2):
            list3_assist.append(arr[i][j])
        list3.append(list3_assist)

        list4_assist = []
        for j in range(len(arr) // 2, len(arr)):
            list4_assist.append(arr[i][j])
        list4.append(list4_assist)

    whole_list.append(list1)
    whole_list.append(list2)
    whole_list.append(list3)
    whole_list.append(list4)

    for arr_block in whole_list:

        if equal_in_number(arr_block) : # 모든 숫자가 같음
            if arr_block[0][0] == 0:
                count_0 += 1
            else:
                count_1 += 1

        elif len(arr_block) == 1 : # 더 이상 줄일 수 없음
            count_0 += arr_block.count(0)
            count_1 += arr_block.count(1)

        else : # 더 줄여야 함
            recursive_quarter(arr_block)


def solution(array):
    answer = []
    global count_0
    global count_1

    if equal_in_number(array):
        if array[0][0] == 0:
            count_0 += 1
        else:
            count_1 += 1
    else:
        recursive_quarter(array)

    return [count_0,count_1]

array = [[1,1,0,0],
       [1,0,0,0],
       [1,0,0,1],
       [1,1,1,1]]
array = [[1,1,1,1,1,1,1,1],
        [0,1,1,1,1,1,1,1],
        [0,0,0,0,1,1,1,1],
        [0,1,0,0,1,1,1,1],
        [0,0,0,0,0,0,1,1],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,1,0,0,1],
        [0,0,0,0,1,1,1,1]]
print(solution(array))



'''
내 코드도 만점이 나왔지만
다른 사람 코드를 보는 중 내 로직보다 괜찮다고 느껴져서
배울 겸 붙여놓았다.

result = []

def check(n, x, y, arr):
    num = arr[x][y]  # 기준값
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 하나라도 다른 원소가 있으면 다시 4개로 나누어 실행
            if num != arr[i][j]:
                check(n//2, x, y, arr)
                check(n//2, x, y + n//2, arr)
                check(n//2, x + n//2, y, arr)
                check(n//2, x + n//2, y + n//2, arr)
                return
    result.append(num)

def solution(arr):
    n = len(arr)  # 정사각형 한 변의 길이
    check(n, 0, 0, arr)
    answer = [0, 0]
    for v in result:
        if v == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer


'''