public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        ArrayList<Integer> emptySet = new ArrayList<>();
        res.add(emptySet);
        Arrays.sort(nums);
        getSubsets(res, emptySet, nums, 0);
        return res;
    }

    private void getSubsets(List<List<Integer>> res, ArrayList<Integer> curSet, int[] nums, int pos) {
        for (int i = pos; i < nums.length; i++) {
            if (i > pos && nums[i] == nums[i - 1])
                continue;
            ArrayList<Integer> tmp = new ArrayList<>(curSet);
            tmp.add(nums[i]);
            res.add(tmp);
            getSubsets(res, tmp, nums, i + 1);
        }
    }
}
