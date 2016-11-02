public class Solution {
    public int longestConsecutive(int[] nums) {
        HashMap<Integer, Boolean> map = new HashMap<>();
        for (int num : nums) {
            map.put(num, false);
        }
        int curLen = 0;
        int maxLen = 0;
        int val;
        for (Integer v : map.keySet()) {
            if (!map.get(v)) {
                val = v;
                curLen = 1;
                while (map.containsKey(val - 1)) {
                    map.put(val - 1, true);
                    curLen++;
                    val--;
                }
                val = v;
                while (map.containsKey(val + 1)) {
                    map.put(val + 1, true);
                    curLen++;
                    val++;
                }
                maxLen = Math.max(maxLen, curLen);
            }
        }
        return maxLen;
    }
}
