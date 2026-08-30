class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d = {}
        for i ,x in enumerate(nums):
            if x not in d:
                d[x] = [i,i]
            else:
                d[x][1] = i
        return sum(b-a+1==nums.count(x) for x,(a,b) in d.items())
