public class Solution {
    public int longestPalindrome(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        char c;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        int len = 0;
        int val;
        boolean hasOdd = false;
        for (char key : map.keySet()) {
            val = map.get(key);
            if (val % 2 == 0) {
                len += val;
            } else {
                hasOdd = true;
                len += (val - 1);
            }
        }
        return hasOdd ? len + 1 : len;
    }
}
