class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            temp = num
            maxi = 0
            digits = 0
            while temp > 0:
                rem = temp % 10
                if rem > maxi:
                    maxi = rem
                digits += 1
                temp //= 10
            encrypted = 0
            while digits > 0:
                encrypted = encrypted * 10 + maxi
                digits -= 1
            ans += encrypted
        return ans