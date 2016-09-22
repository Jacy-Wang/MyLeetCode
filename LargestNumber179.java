public class Solution {
    public String largestNumber(int[] nums) {
        if (nums.length == 0)
            return "0";
        String[] s = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            s[i] = Integer.toString(nums[i]);
        }
        Arrays.sort(s, new Comparator<String>(){
            public int compare(String s1, String s2) {
                return (s1 + s2).compareTo(s2 + s1);
            }
        });
        StringBuilder sb = new StringBuilder();
        for (int i = s.length - 1; i >= 0; i--) {
            sb.append(s[i]);
        }
        String res = sb.toString();
        return res.charAt(0) == '0' ? "0" : res;
    }
}
