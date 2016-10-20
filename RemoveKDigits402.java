public class Solution {
    public String removeKdigits(String num, int k) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < num.length(); i++) {
            sb.append(num.charAt(i));
        }
        char c;
        int counter = 0;
        int i = 0;
        while (i < sb.length() - 1) {
            c = sb.charAt(i);
            if (counter < k) {
                if (c > sb.charAt(i + 1)) {
                    counter++;
                    sb.deleteCharAt(i);
                    if (i != 0) {
                        i--;
                    }
                } else {
                    i++;
                }
            } else {
                break;
            }
        }
        while (counter < k && sb.length() > 0) {
            sb.deleteCharAt(sb.length() - 1);
            counter++;
        }
        while (sb.length() > 0 && sb.charAt(0) == '0') {
            sb.deleteCharAt(0);
        }
        return sb.length() == 0 ? "0" : sb.toString();
    }
}
