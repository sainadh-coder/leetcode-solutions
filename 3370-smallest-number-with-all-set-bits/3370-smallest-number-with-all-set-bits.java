class Solution {
    public int smallestNumber(int n) {
        for (int i = 0; i <= n; i++) {
            int value = (int)Math.pow(2, i) - 1;
            if (value >= n) {
                return value;
            }
        }
        return -1;
    }
}
