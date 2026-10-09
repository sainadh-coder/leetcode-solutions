
import java.util.Stack;

class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> s = new Stack<>();

        int n = tokens.length;

        for (int i = 0; i < n; i++) {
            if (tokens[i].equals("+")) {
                int a = s.pop();
                int b = s.pop();
                s.push(b + a);
            }
            else if (tokens[i].equals("-")) {
                int a = s.pop();
                int b = s.pop();
                s.push(b - a);
            }
            else if (tokens[i].equals("*")) {
                int a = s.pop();
                int b = s.pop();
                s.push(b * a);
            }
            else if (tokens[i].equals("/")) {
                int a = s.pop();
                int b = s.pop();
                s.push(b / a);
            }
            else {
                s.push(Integer.parseInt(tokens[i]));
            }
        }

        return s.pop();
    }
}
