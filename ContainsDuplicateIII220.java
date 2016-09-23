public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (nums.length < 2 || k < 1 || t < 0)
            return false;
        TreeSet<Long> mySet = new TreeSet<>();
        for (int i = 0; i < nums.length; i++) {
            long cur = (long) nums[i];
            if (mySet.floor(cur) != null && cur - t <= mySet.floor(cur))
                return true;
            if (mySet.ceiling(cur) != null && mySet.ceiling(cur) <= t + (long) cur)
                return true;
            mySet.add(cur);
            if (i >= k) {
                mySet.remove((long) nums[i - k]);
            }
        }
        return false;
    }
}
