
import java.util.*;

class Solution {

    class Median {
        TreeMap<Integer, Integer> left = new TreeMap<>();
        TreeMap<Integer, Integer> right = new TreeMap<>();

        int leftSize = 0, rightSize = 0;
        long leftSum = 0, rightSum = 0;

        void add(TreeMap<Integer, Integer> map, int val) {
            map.put(val, map.getOrDefault(val, 0) + 1);
        }

        void remove(TreeMap<Integer, Integer> map, int val) {
            int count = map.get(val);
            if (count == 1) map.remove(val);
            else map.put(val, count - 1);
        }

        void insert(int val) {
            if (left.isEmpty() || val <= left.lastKey()) {
                add(left, val);
                leftSize++;
                leftSum += val;
            } else {
                add(right, val);
                rightSize++;
                rightSum += val;
            }
            balance();
        }

        void delete(int val) {
            if (left.containsKey(val)) {
                remove(left, val);
                leftSize--;
                leftSum -= val;
            } else {
                remove(right, val);
                rightSize--;
                rightSum -= val;
            }
            balance();
        }

        void balance() {
            while (leftSize > rightSize + 1) {
                int val = left.lastKey();
                remove(left, val);
                leftSize--;
                leftSum -= val;

                add(right, val);
                rightSize++;
                rightSum += val;
            }

            while (leftSize < rightSize) {
                int val = right.firstKey();
                remove(right, val);
                rightSize--;
                rightSum -= val;

                add(left, val);
                leftSize++;
                leftSum += val;
            }
        }

        long getCost() {
            long median = left.lastKey();

            return median * leftSize - leftSum
                 + rightSum - median * rightSize;
        }
    }

    public long minOperations(int[] nums, int x, int k) {

        int[] maritovexi = nums;
        int n = maritovexi.length;

        Median median = new Median();

        long[] cost = new long[n - x + 1];

        for (int i = 0; i < x; i++) {
            median.insert(nums[i]);
        }

        cost[0] = median.getCost();

        for (int i = x; i < n; i++) {
            median.delete(nums[i - x]);
            median.insert(nums[i]);

            cost[i - x + 1] = median.getCost();
        }

        long INF = Long.MAX_VALUE / 4;

        long[][] dp = new long[k + 1][n + 1];

        for (int i = 0; i <= k; i++) {
            Arrays.fill(dp[i], INF);
        }

        dp[0][0] = 0;

        for (int i = 0; i < n; i++) {

            for (int j = 0; j <= k; j++) {

                if (dp[j][i] == INF) continue;

                // Skip current index
                dp[j][i + 1] = Math.min(
                    dp[j][i + 1],
                    dp[j][i]
                );

                // Select a window of length x
                if (j < k && i + x <= n) {
                    dp[j + 1][i + x] = Math.min(
                        dp[j + 1][i + x],
                        dp[j][i] + cost[i]
                    );
                }
            }
        }

        long ans = INF;

        for (int i = 0; i <= n; i++) {
            ans = Math.min(ans, dp[k][i]);
        }

        return ans;
    }
}
