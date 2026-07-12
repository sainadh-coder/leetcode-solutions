import java.util.*;
class Solution {
    public char processStr(String s, long k) {
        int n = s.length();
        long[] len = new long[n];
        long cur = 0;
        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);

            if (ch >= 'a' && ch <= 'z') {
                cur++;
            } else if (ch == '*') {
                if (cur > 0) cur--;
            } else if (ch == '#') {
                cur = Math.min(cur * 2, (long) 1e18);
            } else { 
            }
            len[i] = cur;
        }
        if (k >= cur) return '.';
        for (int i = n - 1; i >= 0; i--) {
            char ch = s.charAt(i);

            long before = (i == 0) ? 0 : len[i - 1];
            long after = len[i];

            if (ch >= 'a' && ch <= 'z') {
                if (k == before) {
                    return ch;
                }
            } else if (ch == '*') {
            } else if (ch == '#') {
                if (k >= before) {
                    k -= before;
                }
            } 
            else { 
                if (before > 0) {
                    k = before - 1 - k;
                }
            }
        }
        return '.';
    }
}