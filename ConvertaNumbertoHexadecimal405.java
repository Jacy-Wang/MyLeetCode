public class Solution {
    public String toHex(int num) {
        int n = 16;
        int val = (num >= 0) ? num : num - Integer.MIN_VALUE;
        StringBuilder sb = new StringBuilder();
        //HashMap<Integer, Character> map = new HashMap<>();
        char[] map = new char[n];
        for (int i = 0; i < n; i++) {
            if (i < 10) {
                map[i] = (char) ('0' + i);
            } else if (i == 10) {
                map[i] = 'a';
            } else if (i == 11) {
                map[i] = 'b';
            } else if (i == 12) {
                map[i] = 'c';
            } else if (i == 13) {
                map[i] = 'd';
            } else if (i == 14) {
                map[i] = 'e';
            } else {
                map[i] = 'f';
            }
        }
        int q = val / n;
        int r = val % n;
        while (q >= n) {
            sb.insert(0, map[r]);
            r = q % n;
            q /= n;
        }
        sb.insert(0, map[r]);
        if (num < 0) {
            sb.insert(0, map[q + 8]);
            while (sb.length() < 8) {
                sb.insert(1, '0');
            }
        } else {
            sb.insert(0, map[q]);
        }
        while (sb.length() > 0 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
