public class Solution {
    public double myPow(double x, int n) {
        if (n >= 0) {
            return powHelper(x, n);
        } else {
            return 1.0 / powHelper(x, -n);
        }
    }

    private double powHelper(double base, int index) {
        if (index == 0) {
            return 1d;
        } else {
            double half = powHelper(base, index / 2);
            return half * half * (index % 2 == 0 ? 1.0 : base);
        }
    }
}
