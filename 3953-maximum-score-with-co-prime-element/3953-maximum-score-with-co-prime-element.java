class Solution {
    public int maxScore(int[] nums, int maxVal) {
        int n = nums.length;
        int[] meratolvic = nums;
        int limit = 100000;
        int[] freq = new int[limit + 1];
        for (int v : nums) freq[v]++;
        int[] cntDiv = new int[limit + 1];
        for (int d = 1; d <= limit; d++) {
            for (int multiple = d; multiple <= limit; multiple += d) {
                cntDiv[d] += freq[multiple];
            }
        }
        int[] mu = mobius(limit);
        long ans = Long.MIN_VALUE;
        for (int x = 1; x <= limit; x++) {
            if (x > maxVal && freq[x] == 0) continue;
            int coprimeCount = 0;
            for (int d = 1; (long) d * d <= x; d++) {
                if (x % d != 0) continue;
                coprimeCount += mu[d] * cntDiv[d];
                int other = x / d;
                if (other != d) {
                    coprimeCount += mu[other] * cntDiv[other];
                }
            }
            int bad = n - coprimeCount;
            int cost;
            if (freq[x] > 0) {
                cost = (x == 1) ? 0 : bad - 1;
            } else {
                cost = (bad > 0) ? bad : 1;
            }
            ans = Math.max(ans, (long) x - cost);
        }
        return (int) ans;
    }
    private int[] mobius(int n) {
        int[] mu = new int[n + 1];
        int[] primes = new int[n + 1];
        boolean[] composite = new boolean[n + 1];
        int pc = 0;
        mu[1] = 1;
        for (int i = 2; i <= n; i++) {
            if (!composite[i]) {
                primes[pc++] = i;
                mu[i] = -1;
            }
            for (int j = 0; j < pc; j++) {
                int p = primes[j];
                long v = (long) i * p;
                if (v > n) break;
                composite[(int) v] = true;
                if (i % p == 0) {
                    mu[(int) v] = 0;
                    break;
                } else {
                    mu[(int) v] = -mu[i];
                }
            }
        }
        return mu;
    }
}