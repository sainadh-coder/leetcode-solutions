from typing import List

class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        base = n + 2

        bit = [0] * (2 * n + 10)

        def update(i):
            while i < len(bit):
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        pref = 0
        ans = 0

        update(base)

        for x in nums:
            if x == target:
                pref += 1
            else:
                pref -= 1

            ans += query(pref + base - 1)
            update(pref + base)

        return ans