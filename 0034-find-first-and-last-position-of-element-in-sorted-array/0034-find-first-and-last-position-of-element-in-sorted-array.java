import java.util.*;

class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = {-1, -1};
        int start = search(nums, target, true);
        int end = search(nums, target, false);
        ans[0] = start;
        ans[1] = end;
        return ans;
    }

    int search(int[] nums, int target, boolean findStartIndex) {
        int start = 0;
        int end = nums.length - 1;
        int ans = -1; // store found index (first/last depending on flag)

        while (start <= end) {
            int mid = start + (end - start) / 2;

            if (target < nums[mid]) {
                end = mid - 1;
            } else if (target > nums[mid]) {
                start = mid + 1;
            } else {
                // found one occurrence
                ans = mid;
                if (findStartIndex) {
                    // move left to find first occurrence
                    end = mid - 1;
                } else {
                    // move right to find last occurrence
                    start = mid + 1;
                }
            }
        }
        return ans;
    }

   
}
