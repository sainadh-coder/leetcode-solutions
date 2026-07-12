class Solution {
    public int[] scoreValidator(String[] events) {
        int wickets = 0;
        int totalScore = 0;
        for (int i = 0; i < events.length; i++) {
            if (events[i].equals("W")) {
                wickets++;
            }
            else if (events[i].equals("WD") || events[i].equals("NB")) {
                totalScore++;
            }
            else {
                totalScore += Integer.parseInt(events[i]);
            }
            if(wickets==10){
                break;
            }
        }
        return new int[]{totalScore, wickets};
    }
}