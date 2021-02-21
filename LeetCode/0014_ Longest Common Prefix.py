class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        strs.sort(key=len)
        result = ''
        idx = 0

        # 제일 작은 크기의 단어를 비교를 위해 뽑음
        origin = strs.pop(0)
        while idx < len(origin):

            for sub_s in strs: # for-else 구문
                if origin[idx] != sub_s[idx]:
                    return result
            else:
                result += origin[idx]

            idx += 1

        return result



# 오답으로 되었던 풀이
# 부분 문자열이 위치에 상관없이 있기만 하면 된다고 이해했음
# strs.sort()
# shortest_str = strs.pop(0)
# max_str = ''
#
# for i in range(len(shortest_str)):
#     for j in range(i+1,len(shortest_str)+1):
#
#         sub_str = shortest_str[i:j]
#         if len(sub_str) < len(max_str):
#             break
#
#         for word in strs:
#             if sub_str not in word:
#                 break
#         else:
#             max_str = max(max_str,sub_str)
#
# return max_str

