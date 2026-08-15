class Solution:
    def kthDigit(self, k: int) -> int:
        if k <= 9:
            return k

        k -= 9
        digit_len = 2
        count = 90

        while k > count * digit_len:
            k -= count * digit_len
            digit_len += 1
            count *= 10

        start = 10 ** (digit_len - 1)

        index = (k - 1) // digit_len
        pos = (k - 1) % digit_len

        num = start + index

        block = num // 10

        if block % 2 == 1:
            num = block * 10 + 9 - (num % 10)

        return int(str(num)[pos])