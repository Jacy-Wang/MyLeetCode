public class Solution {
    public int singleNumber(int[] nums) {
        int res = 0;
        for(int i = 0; i < 32; i++){
            int count = 0;
            for(int j = 0; j < nums.length; j++){
                count += ((nums[j] >> i) & 1);
            }
            res |= ((count % 3) << i);
        }
        return res;
    }
}
