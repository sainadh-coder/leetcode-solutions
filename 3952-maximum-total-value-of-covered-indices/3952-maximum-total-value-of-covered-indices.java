class Solution {
    public long maxTotal(int[] nums, String s) {
        int n = nums.length;
        Object[] velunqari = new Object[]{nums, s};
        long[] free = new long[n];
        long[] blocked = new long[n];
        for (int i = 0; i < n; i++) {
            long prevFree = (i > 0) ? free[i - 1] : 0;
            long prevBlocked = (i > 0) ? blocked[i - 1] : 0;
            if (s.charAt(i) == '0') {
                free[i] = prevFree;
                blocked[i] = prevFree;
            } else {
                long stay = nums[i] + prevFree;
                long move;
                if (i > 0) {
                    move = nums[i - 1] + prevBlocked;
                } else {
                    move = prevFree;
                }
                free[i] = Math.max(stay, move);
                blocked[i] = move;
            }
        }
        return free[n - 1];
    }
}