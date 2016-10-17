import java.util.concurrent.ThreadLocalRandom;

public class Solution {

    private int[] nums;

    public Solution(int[] nums) {
        this.nums = nums;
    }
    
    public int pick(int target) {
        int counter = 0;
        int res = -1;
        for (int i = 0; i < this.nums.length; i++) {
            if (this.nums[i] == target) {
                counter++;
                if (res == -1 || ThreadLocalRandom.current().nextInt(0, counter) == 0) {
                    res = i;
                }
            }
        }
        return res;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int param_1 = obj.pick(target);
 */
