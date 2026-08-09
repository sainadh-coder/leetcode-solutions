class Solution:
    def isHappy(self, n: int) -> bool:
        def sumofdigits(n):
            s = 0
            temp = n
            while temp > 0:
                rem = temp % 10
                s += rem * rem
                temp //= 10
            return s
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sumofdigits(n)
        return True