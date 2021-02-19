class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        digit_to_letters = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = set()
        mapper = []  # all possible letter
        for digit in digits:
            mapper += digit_to_letters[digit]

        # n개중 m개 뽑도록 하기
        n = len(mapper)
        m = len(digits)
        possible_letter_idx = []

        # Create letters based on a given index (combination -> possible_letter_idx)
        def mapping():
            temp = ""  # Where the letters will be stored.
            sub_digits = ''  # to search wrong case
            sub_idx = 1

            for idx in possible_letter_idx:
                letter = mapper[idx]
                temp += letter

                # exception_handling ( duplicate position )
                for key in digit_to_letters:
                    if letter in digit_to_letters[key]:
                        sub_digits += key

                if sub_digits != digits[:sub_idx]:
                    return
                sub_idx += 1
                ###########

            if temp:
                result.add(temp)  # a collection of letters

        # make index order
        def combination(curr_num, cnt):
            if curr_num == n:
                if cnt == m:
                    mapping()
                return

            possible_letter_idx.append(curr_num)
            combination(curr_num + 1, cnt + 1)
            possible_letter_idx.pop()

            combination(curr_num + 1, cnt)

        combination(0, 0)

        return list(result)



'''
# 훨씬 간결해보이는 solution
# 백트래킹

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output

'''



'''
# 훨씬 간결해보이는 solution 2 
# 단순 반복문

def letterCombinations(self, digits: str) -> List[str]:

    if not digits:
        return []

    phone = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }

    current_vals = [""]

    for digit in digits:
        next_vals = []
        for val in current_vals:
            for ch in phone[digit]:
                next_vals.append(val + ch)

        current_vals = next_vals

    return current_vals
'''