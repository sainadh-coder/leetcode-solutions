import java.util.*;

class Solution {
    public boolean checkPerfectNumber(int num) {
        List<Integer> l = new ArrayList<>();
        int sum = 0;

        for (int i = 1; i < num; i++) {
            if (num % i == 0) {
                l.add(i);
            }
        }

        for (int j = 0; j < l.size(); j++) {
            sum += l.get(j);
        }

        if(sum==num)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
}
