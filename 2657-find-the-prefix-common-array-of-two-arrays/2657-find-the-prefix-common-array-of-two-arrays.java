import java.util.*;

class Solution {
    public int[] findThePrefixCommonArray(int[] A, int[] B) {
        List<Integer> C = new ArrayList<>();
        int n = A.length;

        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j <= i; j++) {
                for (int k = 0; k <= i; k++) {
                    if (A[j] == B[k]) {
                        count++;
                        break; 
                    }
                }
            }
            C.add(count);
        }

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = C.get(i);
        }
        return result;
    }
}
