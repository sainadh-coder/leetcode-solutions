import java.util.*;
class Solution {
    public int maxLength(List<String> arr) {
        int n = arr.size();
        int max = 0;
        for (int i = 0; i < n; i++) {
            String s = arr.get(i);
            if (unique(s)) {
                max = Math.max(max, s.length());
                for (int j = i + 1; j < n; j++) {
                    String t = s + arr.get(j);
                    if (unique(t)) {
                        max = Math.max(max, t.length());
                    }
                }
            }
        }
        return Math.max(max, solve(arr, 0, ""));
    }
    int solve(List<String> arr, int i, String curr) {
        if (i == arr.size()) {
            return curr.length();
        }
        int skip = solve(arr, i + 1, curr);
        String next = curr + arr.get(i);
        int take = 0;
        if (unique(next)) {
            take = solve(arr, i + 1, next);
        }
        return Math.max(skip, take);
    }
    boolean unique(String s) {
        boolean[] seen = new boolean[26];
        for (int i = 0; i < s.length(); i++) {
            int x = s.charAt(i) - 'a';
            if (seen[x]) {
                return false;
            }
            seen[x] = true;
        }
        return true;
    }
}