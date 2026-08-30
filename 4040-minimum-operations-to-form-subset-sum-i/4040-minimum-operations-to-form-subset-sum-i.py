class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        dp = {0:0}
        for i in nums:
            old = dp.copy()
            p,q = i,0
            while p<=sum:
                for r,k in old.items():
                    if r+p<=sum:
                        dp[r+p] = min(dp.get(r+p,10**9),k+q)
                p*=2
                q+=1
            p,q = i//2,1
            while p:
                for r,k in old.items():
                    if r+p<=sum:
                        dp[r+p] = min(dp.get(r+p,10**9),k+q)
                p//=2
                q+=1
        return dp.get(sum,-1)