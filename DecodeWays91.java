/*
num[i+1] represents the number of decodings for the substring s[0...i]
let x = s[i-1], y = s[i], val = x * 10 + y
if val > 26 && y != 0, num[i+1] = num[i]
if 1 <= val <= 9, num[i+1] = num[i]
if 11 <= val <= 26 && y != 0, num[i+1] = num[i] + num[i - 1]
if y == 0, if x == 1 || x == 2, num[i+1] = num[i-1]
           else, num[i+1] = 0, no possible decoding, return 0.
*/
public class Solution {
    public int numDecodings(String s) {
        if (s.equals("") || s.charAt(0) == '0')
            return 0;       
        int[] num = new int[s.length() + 1];
        num[0] = 1;
        num[1] = 1;
        for (int i = 1; i < s.length(); i++) {
            int val = Integer.parseInt(s.substring(i - 1, i + 1));
            if (val <= 9 || val > 26)
                num[i + 1] = num[i];
            if (val >= 11 && val <= 26)
                num[i + 1] = num[i] + num[i - 1];
            if (s.charAt(i) == '0') {
                if (s.charAt(i - 1) == '1' || s.charAt(i - 1) == '2')
                    num[i + 1] = num[i - 1];
                else
                    return 0;
            }
        }
        return num[s.length()];
    }
}
