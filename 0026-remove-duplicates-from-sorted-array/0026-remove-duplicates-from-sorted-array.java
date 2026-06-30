import java.util.*;

class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length == 0) return 0;

        Arrays.sort(nums); // Optional: Only if input isn't sorted

        int k = 1; // index for the next unique element

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[k - 1]) {
                nums[k] = nums[i];
                k++;
            }
        }

        return k;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input size
        int n = scanner.nextInt();

        // Input array
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) {
            nums[i] = scanner.nextInt();
        }

        Solution sol = new Solution();
        int k = sol.removeDuplicates(nums);

        // Output the first k unique elements
        System.out.println("Number of unique elements: " + k);
        System.out.print("Modified array: ");
        for (int i = 0; i < k; i++) {
            System.out.print(nums[i] + " ");
        }

        scanner.close();
    }
}
