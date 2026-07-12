class Solution {
    public int[] leftRightDifference(int[] nums) {
        int n = nums.length;
        int[] leftsum = new int[n];
        int[] rightsum = new int[n];
        int[] ans  = new int[n];
        for(int i=0;i<n;i++){
            int sum1 = 0;
            for(int j=i+1;j<n;j++){
                sum1+=nums[j];
            }
            rightsum[i] = sum1;
            int sum2 = 0;
            for(int k=i-1;k>=0;k--){
                sum2+=nums[k];
            }
            leftsum[i] = sum2;
        }
        for(int i=0;i<n;i++){
            ans[i] = Math.abs(leftsum[i]-rightsum[i]);
        }
        return ans;
    }
}