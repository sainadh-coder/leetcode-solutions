class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == 1:
            a = [x for x in nums if nums.count(x) == 1]
            return max(a) if a else -1

        if k == len(nums):
            return max(nums)

        ans = -1

        if nums.count(nums[0]) == 1:
            ans = max(ans, nums[0])

        if nums.count(nums[-1]) == 1:
            ans = max(ans, nums[-1])

        return ans