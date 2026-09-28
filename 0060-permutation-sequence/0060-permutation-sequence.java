class Solution {
    public String getPermutation(int n, int k) {
        String up = "";

        for (int i = 1; i <= n; i++) {
            up += i;
        }

        return permutations("", up, k);
    }

    static String permutations(String p, String up, int k) {
        if (up.length() == 1) {
            return p + up;
        }

        int fact = factorial(up.length() - 1);

        int index = (k - 1) / fact;
        k = (k - 1) % fact + 1;

        char ch = up.charAt(index);

        String remaining = up.substring(0, index) + up.substring(index + 1);

        return permutations(p + ch, remaining, k);
    }

    static int factorial(int n) {
        int ans = 1;

        for (int i = 1; i <= n; i++) {
            ans *= i;
        }

        return ans;
    }
}