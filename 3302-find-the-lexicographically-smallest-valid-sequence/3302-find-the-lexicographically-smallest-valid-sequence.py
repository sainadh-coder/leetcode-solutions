from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # suf[i] = maximum suffix of word2 that can still be matched
        # starting from word1[i]
        suf = [m] * (n + 1)
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                j -= 1
            suf[i] = j + 1

        ans = []
        changed = False
        j = 0

        for i in range(n):
            if j == m:
                break

            # Exact match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use the one allowed modification
            elif (not changed) and suf[i + 1] <= j + 1:
                ans.append(i)
                changed = True
                j += 1

        if j == m:
            return ans
        return []