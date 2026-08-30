class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        mod = 10**9 +7
        res = 0
        for i in nums:
            p,q = str(i),i%10
            d = p[:-1]
            res+=pow(int(d[:q]),int(d[q:]),mod)
        return res%mod