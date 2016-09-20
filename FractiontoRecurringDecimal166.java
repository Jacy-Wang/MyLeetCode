public class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        HashMap<Long, Integer> map = new HashMap<>();
        ArrayList<Long> quotient = new ArrayList<>();
        boolean negative = false;
        if ((numerator > 0 && denominator < 0) || (numerator < 0 && denominator > 0)) {
            negative = true;
        }
        long numer = Math.abs((long) numerator);
        long denom = Math.abs((long) denominator);
        int digit = -1;
        int start = -1;
        while (true) {
            long q = numer / denom;
            long r = numer % denom;
            quotient.add(q);
            digit++;
            if (r == 0) {
                break;
            } else {
                if (map.containsKey(r)) {
                    start = map.get(r);
                    break;
                } else {
                    map.put(r, digit);
                    numer = r * 10;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        sb.append(quotient.get(0));
        if (quotient.size() > 1) {
            sb.append(".");
        }
        if (start == -1) {
            for (int i = 1; i < quotient.size(); i++) {
                sb.append(quotient.get(i));
            }
        } else {
            for (int i = 1; i <= start; i++) {
                sb.append(quotient.get(i));
            }
            sb.append("(");
            for (int i = start + 1; i <= digit; i++) {
                sb.append(quotient.get(i));
            }
            sb.append(")");
        }
        if (negative) {
            sb.insert(0, "-");
        }
        return sb.toString();
    }
}
