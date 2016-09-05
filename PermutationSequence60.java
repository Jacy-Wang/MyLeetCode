public class Solution {
    public String getPermutation(int n, int k) {
        int[] res = new int[n];
        int[] factorial = new int[n];
        factorial[0] = 1;
        for (int i = 1; i < n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }
        ArrayList<Integer> mySet = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            mySet.add(i + 1);
        }
        for (int i = 0; i < n; i++) {
            k = getCurrentDigit(i, n, k, factorial, res, mySet);
        }
        StringBuilder sb = new StringBuilder();
        for (int v : res) {
            sb.append(v);
        }
        return sb.toString();
    }

    private int getCurrentDigit(int pos, int n, int k, int[] factorial, int[] res, ArrayList<Integer> mySet) {
        int base = factorial[n - pos - 1];
        int quotient = k / base;
        int residual = k % base;
        int place = residual == 0 ? quotient : quotient + 1;
        res[pos] = mySet.get(place - 1);
        mySet.remove(place - 1);
        return residual == 0 ? k - (quotient - 1) * base : residual;
    }
}
