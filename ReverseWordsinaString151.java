public class Solution {
    public String reverseWords(String s) {
        StringBuilder res = new StringBuilder();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == ' ') {
                if (sb.length() == 0) {
                    continue;
                } else {
                    res.insert(0, sb.toString() + " ");
                    sb.delete(0, sb.length());
                }
            } else {
                sb.append(s.charAt(i));
            }
        }
        if (sb.length() > 0) {
        	res.insert(0, sb.toString() + " ");
        }
        String res2 = res.toString();
        return res2.length() == 0 ? res2 : res2.substring(0, res2.length() - 1);
    }
}
