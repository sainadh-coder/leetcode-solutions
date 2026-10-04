class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        NEG = -10**18
        dp = [[NEG]*2 for _ in range(2)]
        ans = NEG
        for x in nums:
            ndp = [[NEG]*2 for _ in range(2)]
            ndp[0][1] = x
            for d in range(2):
                for p in range(2):
                    if dp[d][p]==NEG:
                        continue
                    val = dp[d][p]+(x if p==0 else -x)
                    ndp[d][p^1]=max(ndp[d][p^1],val)
                    if d==0:
                        ndp[1][p]=max(ndp[1][p],dp[d][p])
            dp = ndp
            ans = max(ans,max(map(max,dp)))
        return ans