class Solution {
    public int countDigits(int num) {
        int p= num;
        int count =0;
        while(p>0){
            int rem = p%10;
            if(num % rem==0){
                count++;
            }
            p/=10;
        }
        return count;
        
    }
}