import java.util.*;
class Solution {
    public int[] closestPrimes(int left, int right) {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = left; i <= right; i++) {
            if (isPrime(i)) {
                arr.add(i);
            }
        }
        if (arr.size() < 2) {
            return new int[]{-1, -1};
        }
        int min = Integer.MAX_VALUE;
        int a = -1, b = -1;
        for (int i = 1; i < arr.size(); i++) {
            int diff = arr.get(i) - arr.get(i - 1);
            if (diff < min) {
                min = diff;
                a = arr.get(i - 1);
                b = arr.get(i);
            }
        }
        return new int[]{a, b};
    }
    static boolean isPrime(int n) {
        if (n < 2) {
            return false;
        }
        if (n == 2) {
            return true;
        }
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }
}