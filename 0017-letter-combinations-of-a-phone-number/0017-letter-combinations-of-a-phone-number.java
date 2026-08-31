import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.isEmpty()) {
            return new ArrayList<>();
        }

        return padRet("", digits);
    }

    static void pad(String p, String up) {
        if (up.isEmpty()) {
            System.out.println(p);
            return;
        }

        int digit = up.charAt(0) - '0';

        String letters = getLetters(digit);

        for (int i = 0; i < letters.length(); i++) {
            char ch = letters.charAt(i);
            pad(p + ch, up.substring(1));
        }
    }

    static ArrayList<String> padRet(String p, String up) {
        if (up.isEmpty()) {
            ArrayList<String> list = new ArrayList<>();
            list.add(p);
            return list;
        }

        int digit = up.charAt(0) - '0';

        String letters = getLetters(digit);

        ArrayList<String> list = new ArrayList<>();

        for (int i = 0; i < letters.length(); i++) {
            char ch = letters.charAt(i);
            list.addAll(padRet(p + ch, up.substring(1)));
        }

        return list;
    }

    static String getLetters(int digit) {
        String[] keypad = {
            "", "", "abc", "def", "ghi",
            "jkl", "mno", "pqrs", "tuv", "wxyz"
        };
        return keypad[digit];
    }
}