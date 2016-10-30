public class Solution {
    public int thirdMax(int[] nums) {
        boolean[] sign = new boolean[3];
        int[] val = new int[3];
        for (int i = 0; i < nums.length; i++) {
            if (!sign[0]) {
                val[0] = nums[i];
                sign[0] = true;
            } else if (!sign[1]) {
                if (nums[i] > val[0]) {
                    val[1] = val[0];
                    val[0] = nums[i];
                    sign[1] = true;
                } else if (nums[i] < val[0]) {
                    val[1] = nums[i];
                    sign[1] = true;
                }
            } else if (!sign[2]) {
                if (nums[i] > val[0]) {
                    val[2] = val[1];
                    val[1] = val[0];
                    val[0] = nums[i];
                    sign[2] = true;
                } else if (nums[i] < val[0] && nums[i] > val[1]) {
                    val[2] = val[1];
                    val[1] = nums[i];
                    sign[2] = true;
                } else if (nums[i] < val[1]) {
                    val[2] = nums[i];
                    sign[2] = true;
                }
            } else {
                if (nums[i] > val[0]) {
                    val[2] = val[1];
                    val[1] = val[0];
                    val[0] = nums[i];
                } else if (nums[i] < val[0] && nums[i] > val[1]) {
                    val[2] = val[1];
                    val[1] = nums[i];
                } else if (nums[i] < val[1] && nums[i] > val[2]) {
                    val[2] = nums[i];
                }
            }
        }
        for (boolean s : sign) {
            System.out.println(s);
        }
        for (int i : val) {
            System.out.println(i);
        }
        return sign[2] ? val[2] : val[0];
    }
}
