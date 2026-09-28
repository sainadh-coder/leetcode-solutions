class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        ans = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
                ans = max(ans, len(stack))
            elif ch == ')':
                stack.pop()
        return ans