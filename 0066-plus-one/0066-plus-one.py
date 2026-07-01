class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for x in digits:
            s += str(x)
        s = str(int(s) + 1)
        ans = []
        for ch in s:
            ans.append(int(ch))
        return ans