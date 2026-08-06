class Solution {
    public int smallestNumber(int n, int t) {
        return product(n, t);
    }

    private int product(int num, int t) {
        int prod = 1;
        int temp = num;

        while (temp > 0) {
            int rem = temp % 10;
            prod *= rem;
            temp /= 10;
        }

        if (prod % t == 0) {
            return num;
        } else {
            return product(num + 1, t);
        }
    }
}