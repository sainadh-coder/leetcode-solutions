from math import gcd
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        n,res = len(nums),0
        for i in range(-1,n):
            p = [0]*n
            q = 0
            for j in range(n-1,-1,-1):
                if j!=i:
                    q = gcd(q,nums[j])
                p[j] = q
            q = 0
            count = 0
            for k in range(n-1):
                if k!=i:
                    q = gcd(q,nums[k])
                if i!=k and q == p[k+1]:
                    count+=1
            res = max(res,count)
        return res
                    