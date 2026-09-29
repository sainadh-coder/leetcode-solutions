class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 == 1:
            return False

        # A valid parentheses string must start with '('
        if grid[0][0] == ')':
            return False

        # dp[j] = set of possible balances at current row/column
        dp = [set() for _ in range(n)]

        dp[0].add(1)

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                cur = set()

                # From top
                if i > 0:
                    cur.update(dp[j])

                # From left
                if j > 0:
                    cur.update(dp[j - 1])

                # Apply current character
                if grid[i][j] == '(':
                    cur = {balance + 1 for balance in cur}
                else:
                    cur = {balance - 1 for balance in cur if balance > 0}

                dp[j] = cur

                if not cur:
                    continue

        return 0 in dp[n - 1]