class Solution {
    public double angleClock(int hour, int minutes) {
        double ha;
        double ma;
        ha = (hour*30) +( 0.5*minutes);
        ma = minutes*6;
        double a = Math.abs(ma-ha);
        double b = 360 - a;
        return Math.min(a,b);
    }
}