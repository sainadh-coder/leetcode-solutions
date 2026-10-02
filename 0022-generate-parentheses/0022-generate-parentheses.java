import java.util.*;

class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<>();
        generate("", 0, 0, n, ans);
        return ans;
    }

    static void generate(String p, int open, int close, int n, List<String> ans) {
        if (p.length() == 2 * n) {
            ans.add(p);
            return;
        }

        if (open < n) {
            generate(p + "(", open + 1, close, n, ans);
        }

        if (close < open) {
            generate(p + ")", open, close + 1, n, ans);
        }
    }
}