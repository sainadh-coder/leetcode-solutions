import java.util.*;

class Solution {
    public String largestNumber(int[] nums) {
        String[] arr = new String[nums.length];

        // convert to strings
        for (int i = 0; i < nums.length; i++) {
            arr[i] = String.valueOf(nums[i]);
        }

        // custom sort
        Arrays.sort(arr, (a, b) -> (b + a).compareTo(a + b));

        // edge case: all zeros
        if (arr[0].equals("0")) {
            return "0";
        }

        // build result
        StringBuilder result = new StringBuilder();
        for (String s : arr) {
            result.append(s);
        }

        return result.toString();
    }
}