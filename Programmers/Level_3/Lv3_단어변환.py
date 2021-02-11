# 모든 단어의 길이는 같음
# 중복된 단어로 주어지지 않음

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    stacks = [begin]
    visited = [0 for i in words]

    while stacks:
        stack = stacks.pop()

        if stack == target:
            return answer

        for word in range(0, len(words)):

            cnt = 0
            for i in range(0,len(words[word])):
                if words[word][i] != stack[i]:
                    cnt += 1

            if cnt == 1:
                if visited[word] != 0:
                    continue
                visited[word] = 1
                stacks.append(words[word])

        answer += 1

    return answer

begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
print(solution(begin,target,words))