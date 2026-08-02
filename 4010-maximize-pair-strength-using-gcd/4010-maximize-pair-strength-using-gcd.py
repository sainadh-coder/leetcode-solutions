import math
class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        max = 0
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                strength = (nums[i]*nums[j])//((math.gcd(nums[i],nums[j]))**2)
                if strength>max:
                    max = strength
        return max