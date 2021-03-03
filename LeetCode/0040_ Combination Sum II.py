class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(remain, stack, candidates):
            if remain == 0 and sorted(stack) not in result:
                result.append(sorted(stack))
                return

            for idx, item in enumerate(candidates):
                if idx > 1 and candidates[idx] == candidates[idx - 1]:
                    continue

                if item > remain:  # candidates의 합이 target보다 큰 경우
                    break
                dfs(remain - item, stack + [item], candidates[idx + 1:])

        result = []
        candidates = sorted(candidates)
        dfs(target, [], candidates)

        return result