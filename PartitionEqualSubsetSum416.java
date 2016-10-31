public class Solution {
    public boolean canPartition(int[] nums) {
        int sum = 0;
        for (int i = 0; i < nums.length; i++) {
            sum += nums[i];
        }
        if (sum % 2 != 0)
            return false;
        HashSet<Integer> set = new HashSet<>();
        set.add(0);
        for (int i = 0; i < nums.length; i++) {
            Integer[] arr = set.toArray(new Integer[0]);
            for (int v : arr)
                set.add(v + nums[i]);
        }
        return set.contains(sum / 2);
    }
}
