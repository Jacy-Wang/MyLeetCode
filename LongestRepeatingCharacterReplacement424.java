public class Solution {
    public int characterReplacement(String s, int k) {
        if (k >= s.length())
            return s.length();
        int end;
        int[] count = new int[26];
        int maxCountIdx = -1;
        int tmp;
        int max = 0;
        for (int i = 0; i < s.length() - k; i++) {
            end = i + k + 1;
            for (int j = 0; j < count.length; j++) {
                count[j] = 0;
            }
            for (int j = i; j < end; j++) {
                tmp = s.charAt(j) - 'A';
                count[tmp]++;
                if (maxCountIdx == -1 || count[tmp] > count[maxCountIdx]) {
                    maxCountIdx = tmp;
                }
            }
            while (end < s.length() && end - i - count[maxCountIdx] <= k) {
                end++;
                tmp = s.charAt(end - 1) - 'A';
                count[tmp]++;
                if (count[tmp] > count[maxCountIdx]) {
                    maxCountIdx = tmp;
                }
            }
            if (end - i - count[maxCountIdx] > k) {
                end--;
            }
            max = Math.max(end - i, max);
        }
        return max;
    }
}
