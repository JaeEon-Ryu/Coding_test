def solution(answers):
    count_correct = [0, 0, 0]

    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx,answer in enumerate(answers):
        if answer == pattern_1[idx%(len(pattern_1))] : count_correct[0]+=1
        if answer == pattern_2[idx%(len(pattern_2))] : count_correct[1]+=1
        if answer == pattern_3[idx%(len(pattern_3))] : count_correct[2]+=1

    max_value = max(count_correct)
    result = [idx +1 for idx,cnt in enumerate(count_correct) if cnt == max_value ]
    return result

#answers = [1,2,3,4,5]
answers = [1,3,2,4,2]
print(solution(answers))
