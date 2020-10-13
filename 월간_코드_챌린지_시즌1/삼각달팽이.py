n=6

def solution(n):
    answer=[]
    array = [[] for row in range(n)]

    i=-1
    num=1

    original_n = n

    down_flag = True
    straight_flag = False
    up_flag = False

    while n!=0:

        hold = (original_n - n) // 3

        if straight_flag:
            for r in range(n):
                array[i].insert(len(array[i])-hold,num)
                num+=1

            straight_flag=False
            up_flag=True

        elif down_flag:
            for r in range(n):
                i += 1
                array[i].insert(len(array[i])-hold,num)
                num += 1

            straight_flag=True
            down_flag=False

        else :
            for r in range(n):
                i -= 1
                array[i].insert(len(array[i])-hold,num)
                num += 1

            up_flag=False
            down_flag=True

        n-=1

    for i in array:
        for j in i:
            answer.append(j)

    for i in array:
        print(i)
    return answer

print(solution(7))
