def solution(arr1, arr2):
    answer = []

    for arr1_row in arr1:
        temp_list = []

        for i in range(len(arr2[0])):
            temp_sum = 0

            for val1,arr2_row in zip(arr1_row,arr2):
                temp_sum += val1*arr2_row[i]

            temp_list.append(temp_sum)
        answer.append(temp_list)

    return answer

#arr1 = [[1,4],[3,2],[4,1]]
#arr2 = [[3,3],[3,3]]

arr1 = [[1,2],[3,4]]
arr2 = [[5,6,7],[8,9,10]]
print(solution(arr1,arr2))