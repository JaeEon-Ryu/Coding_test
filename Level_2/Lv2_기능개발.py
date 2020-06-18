

def solution(progresses, speeds):
    answer = []
    while len(progresses) != 0:
        temp = 0
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        if progresses[0] >= 100:
            for j in range(0, len(progresses)):
                if progresses[j] < 100:
                    break
                temp += 1
        if temp > 0:
            answer.append(temp)
            for k in range(temp):
                progresses.pop(0)
                speeds.pop(0)

    return answer