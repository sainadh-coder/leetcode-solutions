class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> ans = new ArrayList<>();
        for (int num = left; num <= right; num++) {
            int temp = num;
            boolean valid = true;
            while (temp > 0) {
                int rem = temp % 10;
                if (rem == 0 || num % rem != 0) {
                    valid = false;
                    break;
                }
                temp /= 10;
            }
            if (valid) {
                ans.add(num);
            }
        }
        return ans;
    }
}