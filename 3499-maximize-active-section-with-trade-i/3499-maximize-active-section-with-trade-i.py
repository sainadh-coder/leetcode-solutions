class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        # Pad with 1's
        t = "1" + s + "1"

        # Run Length Encoding
        runs = []
        for ch in t:
            if not runs or runs[-1][0] != ch:
                runs.append([ch, 1])
            else:
                runs[-1][1] += 1

        # Count original active sections
        ones = s.count('1')

        best = 0

        # Find the maximum gain
        for i in range(1, len(runs) - 1):
            if (runs[i][0] == '1' and
                runs[i - 1][0] == '0' and
                runs[i + 1][0] == '0'):
                best = max(best, runs[i - 1][1] + runs[i + 1][1])

        return ones + best