import java.util.*;
class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> ans = new ArrayList<>();
        int n = nums.length;
        int p = n / 3;
        Arrays.sort(nums);
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (nums[i] == nums[j]) {
                    count++;
                }
            }
            if (count > p && !ans.contains(nums[i])) {
                ans.add(nums[i]);
            }
        }
        return ans;
    }
}