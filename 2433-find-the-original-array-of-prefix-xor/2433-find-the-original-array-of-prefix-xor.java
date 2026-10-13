class Solution {
    public int[] findArray(int[] pref) {
        int n = pref.length;
        int[] arr = new int[n];
        arr[0] = pref[0];
        for(int i=1;i<n;i++){
            arr[i] = pref[i]^pref[i-1];
        }
        for(int i=0;i<n;i++){
            pref[i] = arr[i];
        }
        return pref;
    }
}