class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        count = 0
        prev = 0

        while n:
            curr = n & 1

            if curr == 1 and prev == 1:
                count += 1
                if count > 1:
                    return False

            prev = curr
            n >>= 1

        return count == 1