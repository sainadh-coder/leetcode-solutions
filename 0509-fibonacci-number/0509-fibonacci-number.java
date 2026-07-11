import java.util.*;

class Solution {
    public int fib(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        List<Integer> f = new ArrayList<>();
        f.add(0); // f[0]
        f.add(1); // f[1]

        for (int i = 2; i <= n; i++) 
        {
            f.add(f.get(i - 1) + f.get(i - 2));
        }

        return f.get(n);
    }
}
