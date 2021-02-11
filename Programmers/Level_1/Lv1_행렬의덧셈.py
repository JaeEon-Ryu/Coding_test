def solution(arr1, arr2):
    answer = []
    for list1, list2 in zip(arr1, arr2):
        temp = []
        for val1, val2 in zip(list1, list2):
            temp.append(val1 + val2)
        answer.append(temp)

    return answer