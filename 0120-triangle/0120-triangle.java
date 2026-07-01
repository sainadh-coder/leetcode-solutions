class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        List<Integer> dp = new ArrayList<>(triangle.get(triangle.size() - 1));

        for (int row = triangle.size() - 2; row >= 0; row--) 
        {
            for (int col = 0; col <= row; col++) 
            {
                int minSum = triangle.get(row).get(col) + Math.min(dp.get(col), dp.get(col + 1));
                dp.set(col, minSum);
            }
        }

        return dp.get(0);
    }
}
