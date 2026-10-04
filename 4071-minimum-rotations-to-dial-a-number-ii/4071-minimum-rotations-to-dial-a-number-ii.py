class Solution:
    def minRotations(self, n: int, s: str) -> int:
        a = list(map(int,s))
        d = lambda x,y:min(abs(x-y),10-abs(x-y))
        suf = [0]*n
        for i in range(n-2,-1,-1):
            suf[i] = suf[i+1]+d(a[i],a[i+1])
        ans = suf[0]+d(0,a[0])
        pref = 0
        for k in range(n):
            prev = 0 if k==0 else a[k-1]
            cost = pref+d(prev,a[n-1])+suf[k]
            ans = min(ans,cost)
            if k<n-1:
                pref+=d(prev,a[k])
        return ans