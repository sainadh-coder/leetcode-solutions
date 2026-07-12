class Solution:
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)

        arr = [1 if x == target else -1 for x in nums]

        ans = 0

        for i in range(n):
            s = 0
            for j in range(i, n):
                s += arr[j]
                if s > 0:
                    ans += 1

        return ans