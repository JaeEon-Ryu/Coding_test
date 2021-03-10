'''
Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
 typically using all the original letters exactly once.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []

        # make dict that includes index information
        # key = index, value = str
        dict_idx_str = dict()
        for i in range(len(strs)):
            dict_idx_str[i] = ''.join(sorted(strs[i]))

        # make dict that includes sorted str information
        # key = str, value = index
        dict_str_idx = dict()
        for idx in dict_idx_str:
            key = dict_idx_str[idx]
            if dict_str_idx.get(key):
                dict_str_idx[key].append(idx)
            else:
                dict_str_idx[key] = [idx]

        # Collection of indexes based on sorted strings
        for idx_list in dict_str_idx.values():
            temp = []
            for idx in idx_list:
                temp.append(strs[idx])

            result.append(temp)

        return result

        '''시간초과가 났던 코드
        result = []
        for s in strs:
            for idx, r in enumerate(result):
                if sorted(r[0]) == sorted(s):
                    result[idx].append(s)
                    break
            else:
                result.append([s])

        return result
        '''

        '''# 리트코드 홈페이지에 올라온 정답 코드
        import collections
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
        
        
        collections 모듈의 defaultdict를 꼭 기억해야겠다.
        굳이 key값이 있는지 일일히 확인하지 않아도 되기 때문에 시간절약에 뛰어나다
        '''
