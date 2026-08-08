class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums2 = []
        for i in range(n - k, n):
            nums2.append(nums[i])
        for i in range(n - k):
            nums2.append(nums[i])
        for i in range(n):
            nums[i] = nums2[i]