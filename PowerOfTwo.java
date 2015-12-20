public class PowerOfTwo {
    public boolean isPowerOfTwo(int n) {
        if (n <= 0) {
            return false;
        }
        else {
            while ((n & 1) == 0) {
                n >>= 1;
            }
            return n == 1;
        }
    }
}