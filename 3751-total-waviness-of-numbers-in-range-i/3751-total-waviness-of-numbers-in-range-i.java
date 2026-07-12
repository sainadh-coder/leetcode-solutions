import java.util.LinkedList;
class Solution {
    public int totalWaviness(int num1, int num2) {
        int wave = 0;
        for (int num = num1; num <= num2; num++) {
            LinkedList<Integer> list = new LinkedList<>();
            int temp = num;
            while (temp > 0) {
                int rem = temp % 10;
                list.addFirst(rem);
                temp /= 10;
            }
            for (int i = 1; i < list.size() - 1; i++) {
                if ((list.get(i) > list.get(i - 1))
                        && (list.get(i) > list.get(i + 1))) {
                    wave++;
                }
                if ((list.get(i) < list.get(i - 1))
                        && (list.get(i) < list.get(i + 1))) {
                    wave++;
                }
            }
        }
        return wave;
    }
}