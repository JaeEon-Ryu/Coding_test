class Solution:
    def intToRoman(self, num: int) -> str:

        mapper = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        result = ''
        while num > 0:
            for value in mapper:
                if num - value >= 0:
                    result += mapper[value]
                    num -= value
                    break

        return result