class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) {
            return false;
        }
        String num = Integer.toString(x); 
        StringBuilder reverseBuilder = new StringBuilder(num);
        reverseBuilder.reverse();
        if (reverseBuilder.toString().equals(num)) {
            return true;
        }
        return false;
    }
}