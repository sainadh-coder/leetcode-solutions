import java.util.*;

class Solution {
    public List<List<Integer>> combine(int n, int k) {
        return combinationsList(new ArrayList<>(), 1, n, k);
    }

    static List<List<Integer>> combinationsList(List<Integer> p, int start, int n, int k) {
        if (p.size() == k) {
            List<List<Integer>> list = new ArrayList<>();
            list.add(new ArrayList<>(p));
            return list;
        }

        List<List<Integer>> ans = new ArrayList<>();

        for (int i = start; i <= n; i++) {
            p.add(i);
            ans.addAll(combinationsList(p, i + 1, n, k));
            p.remove(p.size() - 1);
        }

        return ans;
    }
}