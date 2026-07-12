class Solution {
    int[] digits;
    Node[][][][][] dp;
    static class Node {
        long cnt;
        long waves;
        Node(long c, long w) {
            cnt = c;
            waves = w;
        }
    }
    public long totalWaviness(long num1, long num2) {
        return solve(num2) - solve(num1 - 1);
    }
    long solve(long n) {
        if (n < 0) return 0;
        String s = Long.toString(n);
        digits = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            digits[i] = s.charAt(i) - '0';
        }
        dp = new Node[s.length()][11][11][2][2];
        return dfs(0, 10, 10, 1, 0).waves;
    }
    Node dfs(int pos, int prev, int pprev,
             int tight, int started) {
        if (pos == digits.length) {
            return new Node(1, 0);
        }
        if (dp[pos][prev][pprev][tight][started] != null) {
            return dp[pos][prev][pprev][tight][started];
        }
        int limit = (tight == 1) ? digits[pos] : 9;
        long totalCount = 0;
        long totalWaves = 0;
        for (int d = 0; d <= limit; d++) {
            int ntight =
                    (tight == 1 && d == limit) ? 1 : 0;
            int nstarted =
                    (started == 1 || d != 0) ? 1 : 0;
            long currentWave = 0;
            if (started == 1 &&
                prev != 10 &&
                pprev != 10) {

                if ((prev > pprev && prev > d) ||
                    (prev < pprev && prev < d)) {
                    currentWave = 1;
                }
            }
            int nprev =
                    (nstarted == 1) ? d : 10;
            int npprev =
                    (nstarted == 1) ? prev : 10;
            Node child =
                    dfs(pos + 1,
                        nprev,
                        npprev,
                        ntight,
                        nstarted);

            totalWaves += child.waves;
            totalWaves += currentWave * child.cnt;
            totalCount += child.cnt;
        }
        return dp[pos][prev][pprev][tight][started]
                = new Node(totalCount, totalWaves);
    }
}