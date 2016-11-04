public class Solution {
    public boolean isMatch(String s, String p) {
        if (s.length() == 0) {
            if (p.length() % 2 != 0) {
                return false;
            } else {
                for (int i = 1; i < p.length(); i += 2) {
                    if (p.charAt(i) != '*') {
                        return false;
                    }
                }
                return true;
            }
        }
        if (p.length() == 0)
            return false;
        if (p.length() >= 2 && p.charAt(1) == '*') {
            if (canMatch(s.charAt(0), p.charAt(0))) {
                return isMatch(s.substring(1), p) || isMatch(s, p.substring(2));
            } else {
                return isMatch(s, p.substring(2));
            }
        }
        if (canMatch(s.charAt(0), p.charAt(0))) {
            return isMatch(s.substring(1), p.substring(1));
        } else {
            return false;
        }
    }

    private boolean canMatch(char c1, char c2) {
        if (c1 == c2) {
            return true;
        } else if (c1 == '.' || c2 == '.') {
            return true;
        }
        return false;
    }
}
