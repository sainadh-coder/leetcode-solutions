import java.util.*;

class Solution {
    private static final int MOD = 1_000_000_007;
    private int[] nums;
    private Integer[][][] memo;
    private int n;

    public int subsequencePairCount(int[] nums) {
        this.nums = nums;
        n = nums.length;

        int maxVal = 200;
        memo = new Integer[n][maxVal + 1][maxVal + 1];

        return dfs(0, 0, 0);
    }

    private int dfs(int idx, int g1, int g2) {
        if (idx == n) {
            return (g1 > 0 && g1 == g2) ? 1 : 0;
        }

        if (memo[idx][g1][g2] != null) {
            return memo[idx][g1][g2];
        }

        long ans = 0;
        int x = nums[idx];

        // skip
        ans += dfs(idx + 1, g1, g2);

        // put in seq1
        int ng1 = (g1 == 0) ? x : gcd(g1, x);
        ans += dfs(idx + 1, ng1, g2);

        // put in seq2
        int ng2 = (g2 == 0) ? x : gcd(g2, x);
        ans += dfs(idx + 1, g1, ng2);

        return memo[idx][g1][g2] = (int)(ans % MOD);
    }

    private int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }
}