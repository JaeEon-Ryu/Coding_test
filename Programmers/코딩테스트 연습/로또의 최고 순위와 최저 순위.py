def solution(lottos, win_nums):
    mapper = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    matched = 0

    for num in win_nums:
        if num in lottos:
            matched += 1

    return [mapper[matched + lottos.count(0)], mapper[matched]]