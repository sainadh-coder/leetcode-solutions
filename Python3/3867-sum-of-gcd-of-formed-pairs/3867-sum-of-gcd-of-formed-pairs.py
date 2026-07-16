import math
class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefixGcd = []
        mx = 0
        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(math.gcd(x, mx))
        prefixGcd.sort()
        l, r = 0, len(prefixGcd) - 1
        ans = 0
        while l < r:
            ans += math.gcd(prefixGcd[l], prefixGcd[r])
            l += 1
            r -= 1
        return ans