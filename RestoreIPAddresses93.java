public class Solution {
    public List<String> restoreIpAddresses(String s) {
        ArrayList<String> res = new ArrayList<>();
        if (s.equals("") || s.length() < 4 || s.length() > 12)
            return res;
        find(s, "", res, 0);
        return res;
    }

    private void find(String s, String addr, ArrayList<String> res, int len) {
        if (len == 3) {
            if (isValid(s))
                res.add(addr + s);
        } else {
            for (int i = 0; i < 3 && i < s.length() - 1; i++) {
                String tmp = s.substring(0, i + 1);
                if (isValid(tmp)) {
                    find(s.substring(i + 1), addr + tmp + ".", res, len + 1);
                }
            }
        }
    }

    private boolean isValid(String s) {
        if (s.charAt(0) == '0')
            return s.equals("0");
        int val = Integer.parseInt(s);
        return (val > 0 && val <= 255);
    }
}
