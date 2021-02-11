skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]

def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        sequence = []

        for precede in skill:
            if precede in tree:
                sequence.append(tree.index(precede))
            else:
                sequence.append(27)

        isOrdered = sequence[:]
        isOrdered.sort()

        if sequence == isOrdered :
            answer+=1

    return answer

print(solution(skill,skill_trees))

