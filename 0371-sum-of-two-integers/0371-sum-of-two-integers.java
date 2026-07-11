class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int carry = a & b;       // calculate carry
            a = a ^ b;               // sum without carry
            b = carry << 1;          // move carry to the left
        }
        return a;
    }
}
