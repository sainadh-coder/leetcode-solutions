class Solution {
    public String mapWordWeights(String[] words, int[] weights) {
        StringBuilder ans = new StringBuilder();

        for (String word : words) {
            int total = 0;

            for (char ch : word.toCharArray()) {
                total += weights[ch - 'a'];
            }

            int r = total % 26;

            // 0 -> 'z', 1 -> 'y', ..., 25 -> 'a'
            ans.append((char) ('z' - r));
        }

        return ans.toString();
    }
}