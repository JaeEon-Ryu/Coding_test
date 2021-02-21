import collections


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s

        s = collections.deque(s)

        plate = [
            []
            for _ in range(numRows)
        ]

        r = 1
        go_reverse = False

        while s:
            one_str = s.popleft()
            plate[r - 1].append(one_str)

            if r == 1:
                go_reverse = False
            if r == numRows:
                go_reverse = True

            if go_reverse:
                r -= 1
            else:
                r += 1

        result = ''
        for p in plate:
            result += ''.join(p)

        return result