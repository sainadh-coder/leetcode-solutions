import java.util.*;

class Solution {
    int[][] st;
    int[] log;

    int gcd(int a, int b) {
        while (b != 0) {
            int t = a % b;
            a = b;
            b = t;
        }
        return a;
    }

    int rangeGcd(int l, int r) {
        if (l > r) return 0;
        int k = log[r - l + 1];
        return gcd(st[k][l], st[k][r - (1 << k) + 1]);
    }

    public int maxValidSplits(int[] nums) {
        int n = nums.length;

        int[] pref = new int[n];
        int[] suff = new int[n];

        pref[0] = nums[0];
        for (int i = 1; i < n; i++) {
            pref[i] = gcd(pref[i - 1], nums[i]);
        }

        suff[n - 1] = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            suff[i] = gcd(suff[i + 1], nums[i]);
        }

        log = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            log[i] = log[i / 2] + 1;
        }

        int levels = log[n] + 1;
        st = new int[levels][n];

        for (int i = 0; i < n; i++) {
            st[0][i] = nums[i];
        }

        for (int k = 1; k < levels; k++) {
            int len = 1 << k;
            int half = len >> 1;

            for (int i = 0; i + len <= n; i++) {
                st[k][i] = gcd(st[k - 1][i], st[k - 1][i + half]);
            }
        }

        int answer = 0;

        for (int j = 0; j < n - 1; j++) {
            if (pref[j] == suff[j + 1]) {
                answer++;
            }
        }

        for (int k = 0; k < n; k++) {

            int left = (k > 0) ? pref[k - 1] : 0;
            int right = (k < n - 1) ? suff[k + 1] : 0;

            int totalGcd = gcd(left, right);
            int score = 0;

            if (k > 0 && k < n - 1 &&
                    left == totalGcd &&
                    right == totalGcd) {
                score++;
            }

            if (k >= 2) {

                int lo = 0, hi = k - 2;
                int first = k - 1;

                while (lo <= hi) {
                    int mid = (lo + hi) >>> 1;

                    if (pref[mid] <= totalGcd) {
                        first = mid;
                        hi = mid - 1;
                    } else {
                        lo = mid + 1;
                    }
                }

                if (first <= k - 2 && pref[first] == totalGcd) {

                    lo = first;
                    hi = k - 2;
                    int last = first - 1;

                    while (lo <= hi) {
                        int mid = (lo + hi) >>> 1;

                        int g = gcd(
                                rangeGcd(mid + 1, k - 1),
                                right
                        );

                        if (g == totalGcd) {
                            last = mid;
                            lo = mid + 1;
                        } else {
                            hi = mid - 1;
                        }
                    }

                    if (last >= first) {
                        score += last - first + 1;
                    }
                }
            }

            if (k <= n - 3) {

                int lo = k + 2;
                int hi = n - 1;
                int lastQ = k + 1;

                while (lo <= hi) {
                    int mid = (lo + hi) >>> 1;

                    if (suff[mid] <= totalGcd) {
                        if (suff[mid] == totalGcd) {
                            lastQ = mid;
                        }
                        lo = mid + 1;
                    } else {
                        hi = mid - 1;
                    }
                }

                lo = k + 1;
                hi = n - 2;
                int firstJ = n - 1;

                while (lo <= hi) {
                    int mid = (lo + hi) >>> 1;

                    int g = gcd(
                            left,
                            rangeGcd(k + 1, mid)
                    );

                    if (g == totalGcd) {
                        firstJ = mid;
                        hi = mid - 1;
                    } else {
                        lo = mid + 1;
                    }
                }

                int lastJ = lastQ - 1;

                if (firstJ <= lastJ) {
                    score += lastJ - firstJ + 1;
                }
            }

            answer = Math.max(answer, score);
        }

        return answer;
    }
}