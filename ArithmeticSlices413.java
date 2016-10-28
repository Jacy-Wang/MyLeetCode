public class Solution {
    public int numberOfArithmeticSlices(int[] A) {
        int diff = 0;
        int start = 0;
        int num = 0;
        int tmp = 0;
        for (int i = 1; i < A.length; i++) {
            tmp = A[i] - A[i - 1];
            if (i == 1) {
                diff = tmp;
            } else {
                if (tmp != diff) {
                    if (i - start >= 3) {
                        num += (i - start - 2) * (i - start - 1) / 2;
                    }
                    start = i - 1;
                    diff = tmp;
                }
            }
        }
        if (A.length - start >= 3) {
            num += (A.length - start - 2) * (A.length - start - 1) / 2;
        }
        return num;
    }
}
