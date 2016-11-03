public class Solution {
    public String originalDigits(String s) {
        int[] alphabet = new int[26];
        for (int i = 0; i < 26; i++) {
            alphabet[i] = 0;
        }
        for (int i = 0; i < s.length(); i++) {
            int idx = s.charAt(i) - 'a';
            alphabet[idx]++;
        }
        int[] num = new int[10];
        num[0] = alphabet['z' - 'a'];
        num[2] = alphabet['w' - 'a'];
        num[4] = alphabet['u' - 'a'];
        num[6] = alphabet['x' - 'a'];
        num[8] = alphabet['g' - 'a'];
        num[3] = alphabet['r' - 'a'] - num[4] - num[0];
        num[5] = alphabet['f' - 'a'] - num[4];
        num[1] = alphabet['o' - 'a'] - num[0] - num[4] - num[2];
        num[7] = alphabet['v' - 'a'] - num[5];
        num[9] = alphabet['i' - 'a'] - num[5] - num[6] - num[8];
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < num[i]; j++) {
                sb.append(i);
            }
        }
        return sb.toString();
    }
}
