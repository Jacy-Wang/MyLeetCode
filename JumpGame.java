public class Solution {
    public boolean canJump(int[] nums) {
        int maxIndex = 0;
        for (int i = 0; i < nums.length; i++) {
            if (i > maxIndex || nums.length - 1 <= maxIndex) {
                break;
            }
            maxIndex = Math.max(maxIndex, i + nums[i]);
        }
        return maxIndex >= nums.length - 1 ? true : false;
    }
}
