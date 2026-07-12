import java.util.*;
class Solution {
    public String processStr(String s) {
        List<Character> stack = new ArrayList<>();
        for (char ch : s.toCharArray()) {
            if (ch >= 'a' && ch <= 'z') {
                stack.add(ch);
            } else if (ch == '*') {
                if (!stack.isEmpty()) {
                    stack.remove(stack.size() - 1);
                }
            } else if (ch == '#') {
                // duplicate current stack
                int size = stack.size();
                for (int i = 0; i < size; i++) {
                    stack.add(stack.get(i));
                }
            } else if (ch == '%') {
                Collections.reverse(stack);
            }
        }
        StringBuilder ans = new StringBuilder();
        for (char c : stack) {
            ans.append(c);
        }
        return ans.toString();
    }
}