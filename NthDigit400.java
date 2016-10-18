public class Solution {
    public int findNthDigit(int n) {
        long c = 9;
        long d = 1;
        long v = (long) Math.pow(10, d - 1);
        while (n - c * v * d > 0) {
            n -= (c * v *d);
            d++;
            v = (long) Math.pow(10, d - 1);
        }
        long q = (long) Math.ceil(n * 1.0 / d);
        long r = n % d;
        long num = v + q - 1;
        if (r != 0) {
            long val1 = (long) Math.pow(10, d - r + 1);
            return (int) ((num % val1) / (val1 / 10));
        } else {
            return (int) num % 10;
        }
    }
}
