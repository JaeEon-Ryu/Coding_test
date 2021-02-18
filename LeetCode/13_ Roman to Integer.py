class Solution:
    def romanToInt(self, s: str) -> int:

        mapper = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1
        }

        result = 0
        while s:
            if len(s) > 1:
                str_1 = s[0]
                str_2 = s[1]

                if str_1 + str_2 in mapper:
                    result += mapper[str_1 + str_2]
                    s = s[2:]
                else:
                    result += mapper[str_1]
                    s = s[1:]
            else:
                result += mapper[s[0]]
                s = s[1:]

        return result