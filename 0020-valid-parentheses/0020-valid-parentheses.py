class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                if ch == ')' and stack[-1] == '(':
                    stack.pop()
                elif ch == ']' and stack[-1] == '[':
                    stack.pop()
                elif ch == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0