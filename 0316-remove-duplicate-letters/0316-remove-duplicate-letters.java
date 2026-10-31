class Solution {
    public String removeDuplicateLetters(String s) {
        int[] freq = new int[26];
        boolean[] visited = new boolean[26];

        char[] c = s.toCharArray();
        char[] ans = new char[c.length];

        for (int i = 0; i < c.length; i++) {
            freq[c[i] - 'a']++;
        }

        int slow = -1;

        for (int fast = 0; fast < c.length; fast++) {
            freq[c[fast] - 'a']--;

            if (visited[c[fast] - 'a']) {
                continue;
            }

            while (slow >= 0 &&
                   ans[slow] > c[fast] &&
                   freq[ans[slow] - 'a'] > 0) {

                visited[ans[slow] - 'a'] = false;
                slow--;
            }

            slow++;
            ans[slow] = c[fast];
            visited[c[fast] - 'a'] = true;
        }

        return new String(ans, 0, slow + 1);
    }
}