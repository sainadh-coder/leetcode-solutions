class Solution {
    public int maxDifference(String s) {
        int[] freq = new int[26]; // for 'a' to 'z'

        // Count frequency of each letter
        for (int i = 0; i < s.length(); i++) {
            freq[s.charAt(i) - 'a']++;
        }

        int maxOdd = Integer.MIN_VALUE;
        int minEven = Integer.MAX_VALUE;

        // Traverse the frequency array
        for (int i = 0; i < 26; i++) {
            if (freq[i] > 0) {
                if (freq[i] % 2 == 1) {
                    if (freq[i] > maxOdd) {
                        maxOdd = freq[i];
                    }
                } else {
                    if (freq[i] < minEven) {
                        minEven = freq[i];
                    }
                }
            }
        }

        // Return the maximum difference
        return maxOdd - minEven;
    }
}
