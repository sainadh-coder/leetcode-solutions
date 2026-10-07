import java.util.*;

public class Solution {
    public boolean gcdSort(int[] nums) {
        int n = nums.length;
        int[] sorted = Arrays.copyOf(nums, n);
        Arrays.sort(sorted);

        int max = 0;
        for (int x : nums) {
            max = Math.max(max, x);
        }

        int[] parent = new int[max + 1];

        for (int i = 0; i <= max; i++) {
            parent[i] = i;
        }

        for (int x : nums) {
            int temp = x;

            for (int p = 2; p * p <= temp; p++) {
                if (temp % p == 0) {
                    union(x, p, parent);

                    while (temp % p == 0) {
                        temp /= p;
                    }
                }
            }

            if (temp > 1) {
                union(x, temp, parent);
            }
        }

        for (int i = 0; i < n; i++) {
            if (find(nums[i], parent) != find(sorted[i], parent)) {
                return false;
            }
        }

        return true;
    }

    static int find(int x, int[] parent) {
        if (parent[x] != x) {
            parent[x] = find(parent[x], parent);
        }
        return parent[x];
    }

    static void union(int a, int b, int[] parent) {
        a = find(a, parent);
        b = find(b, parent);

        if (a != b) {
            parent[b] = a;
        }
    }
}