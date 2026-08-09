from math import log10
class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            temp = num
            maxi = 0
            while temp > 0:
                maxi = max(maxi, temp % 10)
                temp //= 10
            digits = int(log10(num)) + 1
            encrypted = 0
            for _ in range(digits):
                encrypted = encrypted * 10 + maxi
            ans += encrypted
        return ans