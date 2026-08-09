class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            temp = num
            maxi = 0
            while temp > 0:
                rem = temp % 10
                if rem > maxi:
                    maxi = rem
                temp //= 10
            temp = num
            place = 1
            encrypted = 0
            while temp > 0:
                encrypted += maxi * place
                place *= 10
                temp //= 10
            ans += encrypted
        return ans