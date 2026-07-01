class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] nums3 = new int[m + n];
        for (int i = 0; i < m; i++) {
            nums3[i] = nums1[i];
        }

        for (int i = 0; i < n; i++) {
            nums3[m + i] = nums2[i];
        }
        for (int i = 0; i < m + n - 1; i++) {
            for (int j = 0; j < m + n - i - 1; j++) {
                if (nums3[j] > nums3[j + 1]) {
                    int temp = nums3[j];
                    nums3[j] = nums3[j + 1];
                    nums3[j + 1] = temp;
                }
            }
        }
        for (int i = 0; i < m + n; i++) {
            nums1[i] = nums3[i];
        }
    }
}
