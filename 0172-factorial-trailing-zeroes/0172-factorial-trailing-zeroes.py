import sys
sys.set_int_max_str_digits(1000000)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0

        product = 1

        for i in range(1, n + 1):
            product *= i

        s = str(product)

        ans = 0

        while s.count('0') > 0 and s[-1] == '0':
            ans += 1
            s = s[:-1]

        return ans