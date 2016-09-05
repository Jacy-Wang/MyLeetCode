public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        int[] sign = new int[nums.length];
        for(int i = 0; i < sign.length; i++) {
            sign[i] = 0;
        }
        ArrayList<Integer> curArr = new ArrayList<>();
        getPermutation(nums, curArr, sign, res);
        return res;
    }

    private void getPermutation(int[] nums, ArrayList<Integer> curArr, int[] sign, List<List<Integer>> res) {
        if (curArr.size() == nums.length) {
            ArrayList<Integer> r = new ArrayList<>();
            for (int i : curArr) {
                r.add(i);
            }
            res.add(r);
        } else {
            for (int i = 0; i < nums.length; i++) {
                if (sign[i] == 0) {
                    if (i > 0 && nums[i] == nums[i - 1] && sign[i - 1] == 1)
                        continue;
                    sign[i] = 1;
                    curArr.add(nums[i]);
                    getPermutation(nums, curArr, sign, res);
                    sign[i] = 0;
                    curArr.remove(curArr.size() - 1);

                }
            }
        }
    }
}
