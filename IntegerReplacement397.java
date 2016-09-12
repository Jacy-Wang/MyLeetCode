public class Solution {
    public int integerReplacement(int n) {
        if (n == 1)
            return 0;
        else if ((n & 1) == 0)
            return integerReplacement(n >>> 1) + 1;
        else
            return Math.min(integerReplacement(n + 1), integerReplacement(n - 1)) + 1;
    }
}
