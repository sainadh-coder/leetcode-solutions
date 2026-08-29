class Solution {
    public String[] largestString(int[] nums) {
        String[] res = new String[nums.length];
        for(int i=0;i<nums.length;i++){
            int p = nums[i];
            StringBuilder sb = new StringBuilder();
            for(int a = 25;a>=0;a--){
                int value = 1<<a;
                while(p>=value){
                    sb.append((char)('a'+a));
                    p-=value;
                }
            }
            res[i] = sb.toString();
        }
        return res;
    }
}