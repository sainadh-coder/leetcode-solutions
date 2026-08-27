class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        ans = []
        for i in range(len(target)):
            t = ord(target[i]) - ord('a')
            if count[t] > 0:
                count[t] -= 1
                ans.append(target[i])
            else:
                break
        if len(ans) < len(target):
            i = len(ans)            
            t = ord(target[i]) - ord('a')
            for c in range(t + 1, 26):
                if count[c] > 0:
                    count[c] -= 1
                    result = ans + [chr(c + ord('a'))]
                    for x in range(26):
                        result.extend([chr(x + ord('a'))] * count[x])
                    return ''.join(result)
        for i in range(len(ans) - 1, -1, -1):
            old = ord(ans[i]) - ord('a')
            count[old] += 1
            for c in range(old + 1, 26):
                if count[c] > 0:
                    count[c] -= 1
                    result = ans[:i] + [chr(c + ord('a'))]
                    for x in range(26):
                        result.extend([chr(x + ord('a'))] * count[x])
                    return ''.join(result)

        return ""