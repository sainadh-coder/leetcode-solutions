class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        else:
            s = ""
            sum = 0
            p = str(n)
            for i in range(len(p)):
                if p[i] != "0":
                    s += p[i]
            for i in range(len(s)):
                sum += int(s[i])
            q = int(s)
            return sum * q 
