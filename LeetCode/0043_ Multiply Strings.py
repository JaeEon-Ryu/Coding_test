'''
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
1. BigInteger 라이브러리를 사용x
2. 입력을 정수로 직접 변환 x
'''


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        digits = [0] * (len(num1) + len(num2))

        for i in range(len(num1) - 1, -1, -1):
            for j in range(len(num2) - 1, -1, -1):
                digits[i + j + 1] += int(num1[i]) * int(num2[j])  # 1의 자리수 임시 저장
                digits[i + j] += digits[i + j + 1] // 10  # 10의 자리수 저장
                digits[i + j + 1] %= 10  # 1의 자리수 저장

        # 공백제거
        i = 0
        while i < len(digits) and digits[i] == 0:
            i += 1

        # 문자형 변환
        result = ''.join([str(num) for num in digits[i:]])

        return result if result else '0'