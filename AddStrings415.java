public class Solution {
    public String addStrings(String num1, String num2) {
        int i1 = num1.length() - 1;
        int i2 = num2.length() - 1;
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        int tmp;
        while (i1 >= 0 && i2 >= 0) {
            tmp = Character.getNumericValue(num1.charAt(i1)) + Character.getNumericValue(num2.charAt(i2)) + carry;
            carry = tmp / 10;
            sb.insert(0, Integer.toString(tmp % 10));
            i1--;
            i2--;
        }
        while (i1 >= 0) {
            tmp = Character.getNumericValue(num1.charAt(i1)) + carry;
            carry = tmp / 10;
            sb.insert(0, Integer.toString(tmp % 10));
            i1--;
        }
        while (i2 >= 0) {
            tmp = Character.getNumericValue(num2.charAt(i2)) + carry;
            carry = tmp / 10;
            sb.insert(0, Integer.toString(tmp % 10));
            i2--;
        }
        if (carry > 0) {
            sb.insert(0, carry);
        }
        return sb.toString();
    }
}
