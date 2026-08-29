from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        arr = sorted((x, i) for i, x in enumerate(nums))
        ans = nums[:]

        i = 0

        while i < len(arr):

            j = i

            while j + 1 < len(arr) and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            indices = sorted(arr[k][1] for k in range(i, j + 1))

            for k, idx in enumerate(indices):
                ans[idx] = arr[i + k][0]

            i = j + 1

        return ans