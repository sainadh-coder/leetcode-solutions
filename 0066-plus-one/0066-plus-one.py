class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ''

        for i in range(len(digits)):
            s += str(digits[i])

        p = int(s)
        p += 1

        q = str(p)
        arr = []

        for i in range(len(q)):
            arr.append(int(q[i]))

        return arr