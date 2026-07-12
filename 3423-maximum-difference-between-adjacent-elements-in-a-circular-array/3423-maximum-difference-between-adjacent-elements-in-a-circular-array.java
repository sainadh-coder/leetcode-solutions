import java.util.*;

class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int n = nums.length;
        List<Integer> diff = new ArrayList<>();

        for (int i = 0; i < n; i++) 
        {
            int j = (i + 1) % n; 
            diff.add(Math.abs(nums[i] - nums[j]));
        }

        return Collections.max(diff); 
    }
}
