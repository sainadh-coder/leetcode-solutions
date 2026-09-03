import java.util.*;

class Solution {
    public List<List<Integer>> permute(int[] nums) {
        ArrayList<Integer> arr = new ArrayList<>();

        for (int num : nums) {
            arr.add(num);
        }

        return permutations(new ArrayList<>(), arr);
    }

    static List<List<Integer>> permutations(List<Integer> p, List<Integer> up) {
        if (up.isEmpty()) {
            ArrayList<List<Integer>> list = new ArrayList<>();
            list.add(p);
            return list;
        }

        int ch = up.get(0);
        ArrayList<List<Integer>> ans = new ArrayList<>();

        for (int i = 0; i <= p.size(); i++) {
            List<Integer> f = new ArrayList<>(p.subList(0, i));
            List<Integer> s = new ArrayList<>(p.subList(i, p.size()));

            f.add(ch);
            f.addAll(s);

            List<Integer> remaining =
                    new ArrayList<>(up.subList(1, up.size()));

            ans.addAll(permutations(f, remaining));
        }

        return ans;
    }
}