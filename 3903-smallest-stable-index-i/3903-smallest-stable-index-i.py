class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            a = nums[0]
            b = nums[i]
            for j in range(i + 1):
                a = max(a, nums[j])
            for p in range(i, len(nums)):
                b = min(b, nums[p])
            if a - b <= k:
                return i
        return -1