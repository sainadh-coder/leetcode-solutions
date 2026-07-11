import java.util.*;

class Solution {
    public List<Integer> lexicalOrder(int n) {
        List<String> strList = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            strList.add(String.valueOf(i));
        }

        Collections.sort(strList);

        List<Integer> result = new ArrayList<>();
        for (String s : strList) {
            result.add(Integer.parseInt(s));
        }

        return result;
    }
}
