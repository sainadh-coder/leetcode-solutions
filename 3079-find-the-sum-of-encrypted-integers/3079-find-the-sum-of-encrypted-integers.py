class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            maxi = max(str(num))
            encrypted = int(maxi * len(str(num)))
            ans += encrypted
        return ans