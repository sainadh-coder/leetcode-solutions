class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(num):
            prod = 1
            temp = num
            while temp > 0:
                rem = temp % 10
                prod *= rem
                temp //= 10
            if prod % t == 0:
                return num
            else:
                return product(num + 1)
        return product(n)