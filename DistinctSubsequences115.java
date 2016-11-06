public class Solution {
    public int numDistinct(String s, String t) {
        if (s.length() < t.length())
            return 0;
        int[][] len = new int[s.length() + 1][t.length() + 1];
        for (int i = 0; i < s.length() + 1; i++) {
            for (int j = 0; j < t.length() + 1; j++) {
                if (i == 0 && j == 0)
                    len[i][j] = 1;
                else if (j == 0)
                    len[i][j] = 1;
                else
                    len[i][j] = 0;
            }
        }
        for (int i = 1; i < s.length() + 1; i++) {
            for (int j = 1; j <= i && j < t.length() + 1; j++) {
                len[i][j] = len[i - 1][j];
                if (s.charAt(i - 1) == t.charAt(j - 1))
                    len[i][j] += len[i - 1][j - 1];
            }
        }
        return len[s.length()][t.length()];
    }
}
