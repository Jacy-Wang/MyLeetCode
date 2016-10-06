public class Solution {
    public int trap(int[] height) {
        if (height.length == 0) {
            return 0;
        }
        int[] leftHighest = new int[height.length];
        leftHighest[0] = 0;
        int highest = height[0];
        for (int i = 1; i < height.length; i++) {
            leftHighest[i] = highest;
            if (height[i] > highest) {
                highest = height[i];
            }
        }
        highest = height[height.length - 1];
        int res = 0;
        for (int i = height.length - 2; i > 0; i--) {
            int tmp = Math.min(highest, leftHighest[i]);
            if (tmp > height[i]) {
                res += (tmp - height[i]);
            }
            if (height[i] > highest) {
                highest = height[i];
            }
        }
        return res;
    }
}
