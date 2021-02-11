import math

def solution(n, words):

    word_set = set()
    preceding_word = words[0][0]

    for leng,word in enumerate(words):
        word_set.add(word)

        if len(word_set) != leng + 1 or word[0] != preceding_word[-1]:
            number = (leng)%n + 1
            turn = math.ceil((leng + 1) / n)
            return [number,turn]

        preceding_word = word

    return [0,0]

n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n,words))