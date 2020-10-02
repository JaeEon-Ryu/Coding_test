expression = "100-200*300-500+20"
import itertools

def operation(num1, num2, op):
    if op == '+' :
        return num1 + num2
    elif op == '-' :
        return num1 - num2
    else :
        return num1 * num2

def solution(expression):
    order_list = ['+', '-', '*']
    order_list = list(itertools.permutations(order_list, 3))

    expression_list = []
    sp = 0
    for idx,i in enumerate(expression):
        if i == '-' or i == '+' or i == '*':
            expression_list.append(int(expression[sp:idx]))
            expression_list.append(i)
            sp = idx + 1
        elif idx == len(expression)-1:
            expression_list.append(int(expression[sp:]))

    answer_list = []

    for order in order_list:
        copy_list = expression_list[:]

        for sign in order:

            while sign in copy_list:
                idx = copy_list.index(sign)
                num1 = copy_list.pop(idx-1)
                num2 = copy_list.pop(idx)
                copy_list.pop(idx-1) # sign

                result = operation(num1,num2,sign)
                copy_list.insert(idx-1,result)

        answer_list.append(abs(copy_list[0]))

    return max(answer_list)

print(solution(expression))