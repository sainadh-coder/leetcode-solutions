class Solution {
    public List<String> buildArray(int[] target, int n) {
        int j = 0;
        int len = target.length;
        List<String> s = new ArrayList();
        for(int i=1;i<=n && j<len;i++){
            s.add("Push");
            if(target[j]==i){
                j++;
            }
            else{
                s.add("Pop");
            }
        }
        return s;
    }
}