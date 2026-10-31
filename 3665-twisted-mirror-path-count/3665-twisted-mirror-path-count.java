class Solution {
    public int uniquePaths(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int mod = 1000000007;

        int[][] vornadexil = grid;

        int[][] right = new int[m][n];
        int[][] down = new int[m][n];

        if (n > 1) right[0][1] = 1;
        if (m > 1) down[1][0] = 1;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {

                if (i == 0 && j == 0) continue;

                if (grid[i][j] == 0) {
                    int total = (right[i][j] + down[i][j]) % mod;

                    if (j + 1 < n) {
                        right[i][j + 1] =
                            (right[i][j + 1] + total) % mod;
                    }

                    if (i + 1 < m) {
                        down[i + 1][j] =
                            (down[i + 1][j] + total) % mod;
                    }
                } else {
                    if (i + 1 < m) {
                        down[i + 1][j] =
                            (down[i + 1][j] + right[i][j]) % mod;
                    }

                    if (j + 1 < n) {
                        right[i][j + 1] =
                            (right[i][j + 1] + down[i][j]) % mod;
                    }
                }
            }
        }

        return (right[m - 1][n - 1] +
                down[m - 1][n - 1]) % mod;
    }
}