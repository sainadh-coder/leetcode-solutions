class Solution {
    int MOD = 1000000007;
    Integer[][] dp;

    public int rearrangeSticks(int n, int k) {
        dp = new Integer[n + 1][k + 1];
        return solve(n, k);
    }

    int solve(int n, int k) {
        if (n == 0 && k == 0) return 1;
        if (n == 0 || k == 0 || k > n) return 0;
        if (dp[n][k] != null) return dp[n][k];

        long a = solve(n - 1, k - 1);
        long b = (long) (n - 1) * solve(n - 1, k);

        return dp[n][k] = (int) ((a + b) % MOD);
    }
}