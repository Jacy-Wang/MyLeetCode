public class Solution {
    public int findMaximumXOR(int[] nums) {
        int mask = 1 << 30;
        ArrayList<Integer> arr0 = new ArrayList<>();
        ArrayList<Integer> arr1 = new ArrayList<>();
        while (mask >= 1) {
            for (int i = 0; i < nums.length; i++) {
                if ((nums[i] & mask) == 0) {
                    arr0.add(nums[i]);
                } else {
                    arr1.add(nums[i]);
                }
            }
            if (arr0.size() > 0 && arr1.size() > 0) {
                break;
            }
            mask >>= 1;
            arr0.clear();
            arr1.clear();
        }
        return getMax(arr0, arr1, mask);
    }

    private void split(ArrayList<Integer> arr, int mask, ArrayList<Integer> res0, ArrayList<Integer> res1) {
        int tmp;
        for (int i = 0; i < arr.size(); i++) {
            tmp = arr.get(i);
            if ((tmp & mask) == 0 ) {
                res0.add(tmp);
            } else {
                res1.add(tmp);
            }
        }
    }

    private int getMax(ArrayList<Integer> arr0, ArrayList<Integer> arr1, int mask) {
        if (mask <= 1)
            return mask;
        mask >>= 1;
        ArrayList<Integer> arr00 = new ArrayList<>();
        ArrayList<Integer> arr01 = new ArrayList<>();
        ArrayList<Integer> arr10 = new ArrayList<>();
        ArrayList<Integer> arr11 = new ArrayList<>();
        split(arr0, mask, arr00, arr01);
        split(arr1, mask, arr10, arr11);
        int res = 0;
        if (arr00.size() > 0 && arr11.size() > 0) {
            res = Math.max(res, getMax(arr00, arr11, mask));
        }
        if (arr01.size() > 0 && arr10.size() > 0) {
            res = Math.max(res, getMax(arr10, arr01, mask));
        }
        if (res == 0) {
            res = getMax(arr0, arr1, mask) - mask;
        }
        return res + 2 * mask;
    }
}
