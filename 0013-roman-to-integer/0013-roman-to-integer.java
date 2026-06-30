class Solution {
    public int romanToInt(String s) {
        char[] symbols = {'I', 'V', 'X', 'L', 'C', 'D', 'M'};
        int[] values = {1, 5, 10, 50, 100, 500, 1000};

        int total = 0;
        int prev = 0;

        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            int curr = 0;

            for (int j = 0; j < symbols.length; j++) {
                if (symbols[j] == c) {
                    curr = values[j];
                    break;
                }
            }

            if (curr < prev) {
                total -= curr;
            } else {
                total += curr;
            }

            prev = curr;
        }

        return total;
    }
}
