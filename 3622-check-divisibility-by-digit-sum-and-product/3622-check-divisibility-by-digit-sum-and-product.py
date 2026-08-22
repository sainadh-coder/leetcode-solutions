class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        sum1 = 0
        prod = 1
        while temp>0:
            rem = temp%10
            sum1+=rem
            prod*=rem
            temp//=10
        if n%(sum1+prod)!=0:
            return False
        return True
