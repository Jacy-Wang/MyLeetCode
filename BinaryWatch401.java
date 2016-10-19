public class Solution {
    public List<String> readBinaryWatch(int num) {
        ArrayList<String> res = new ArrayList<>();
        for (int v = 0; v < 1024; v++) {
            if (Integer.bitCount(v) == num) {
                int h = v >>> 6;
                int m = v & 0x3F;
                if (h < 12 && m < 60) {
                    res.add(String.format("%d:%02d", h, m));
                }
            }
        }
        return res;
    }
}
