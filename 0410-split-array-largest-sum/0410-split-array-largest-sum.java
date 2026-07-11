class Solution {
    public int splitArray(int[] nums, int k) {
        int start = 0;
        int end = 0;

        // Find start (max element) and end (total sum)
        for (int num : nums) {
            start = Math.max(start, num);
            end += num;
        }

        // Binary search between max element and total sum
        while (start < end) {
            int mid = start + (end - start) / 2;

            int sum = 0;
            int pieces = 1;

            // Count how many subarrays are needed for this mid
            for (int num : nums) {
                if (sum + num > mid) {
                    sum = num;
                    pieces++;
                } else {
                    sum += num;
                }
            }

            // If too many pieces, we need a larger max sum → move right
            if (pieces > k) {
                start = mid + 1;
            } else {
                end = mid;  // we can try smaller sums
            }
        }

        return start; // or end, both are same when loop ends
    }
}
