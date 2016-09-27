public class Solution {
    public boolean increasingTriplet(int[] nums) {
        boolean s1 = false;
        boolean s2 = false;
        int small = 0;
        int second = 0;
        for (int num : nums) {
            if (!s1 || num <= small) {
                small = num;
                s1 = true;
            } else if (!s2 || num <= second) {
                second = num;
                s2 = true;
            } else {
                return true;
            }
        }
        return false;
    }
}
