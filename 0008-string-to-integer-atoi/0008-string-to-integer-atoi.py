class Solution:
    def myAtoi(self, s: str) -> int:
        ans = ""
        i = 0
        while i < len(s) and s[i] == " ":
            i += 1
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            ans += s[i]
            i += 1
        while i < len(s) and s[i].isdigit():
            ans += s[i]
            i += 1
        if ans == "" or ans == "+" or ans == "-":
            return 0
        num = int(ans)
        INT_MIN = -(2 ** 31)
        INT_MAX = 2 ** 31 - 1
        return max(INT_MIN, min(INT_MAX, num))