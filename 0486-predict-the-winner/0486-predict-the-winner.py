from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        @lru_cache(None)
        def dfs(i, j):
            if i == j:
                return nums[i]

            takeLeft = nums[i] - dfs(i + 1, j)
            takeRight = nums[j] - dfs(i, j - 1)

            return max(takeLeft, takeRight)

        return dfs(0, len(nums) - 1) >= 0