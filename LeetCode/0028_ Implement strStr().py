class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.index(needle) if needle in haystack else -1





    '''
    내장 함수를 쓰지 않았을 때 ( baby_groot - 참고 )

    
    def strStr2(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    def kmp(str_):
        b, prefix = 0, [0]
        for i in range(1, len(str_)):
            while b > 0 and str_[i] != str_[b]:
                b = prefix[b - 1]
            if str_[b] == str_[i]:
                b += 1
            else:
                b = 0
            prefix.append(b)
        return prefix

    str_ = kmp(needle + '#' + haystack)
    n = len(needle)
    if n == 0:
        return n
    for i in range(n + 1, len(str_)):
        if str_[i] == n:
            return i - 2 * n
    return -1
    
    '''