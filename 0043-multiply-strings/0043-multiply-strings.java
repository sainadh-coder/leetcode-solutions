class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) return "0";
        int[] result = new int[num1.length() + num2.length()];
        for (int i = num1.length() - 1; i >= 0; i--) 
        {
            int digit1 = num1.charAt(i) - '0';

            for (int j = num2.length() - 1; j >= 0; j--) 
            {
                int digit2 = num2.charAt(j) - '0';
                int sum = digit1 * digit2 + result[i + j + 1];

                result[i + j + 1] = sum % 10; // Set the current digit
                result[i + j] += sum / 10;    // Carry over to the next left digit
            }
        }

        // Convert result array to string
        StringBuilder sb = new StringBuilder();
        for (int digit : result) {
            if (!(sb.length() == 0 && digit == 0)) { // Skip leading zeros
                sb.append(digit);
            }
        }

        return sb.toString();
    }
}
