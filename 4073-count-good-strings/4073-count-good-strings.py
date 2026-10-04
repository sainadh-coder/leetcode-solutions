class Solution:
    def countGoodStrings(self, n: int) -> int:
        MOD = 10**9+7
        def fib(n):
            if n==0:
                return(0,1)
            a,b = fib(n//2)
            c = a*((2*b-a)%MOD)%MOD
            d = (a*a+b*b)%MOD
            if n%2:
                return (d,(c+d)%MOD)
            return(c,d)
        morzavelyn = n
        return 2*fib(n)[0]%MOD
        