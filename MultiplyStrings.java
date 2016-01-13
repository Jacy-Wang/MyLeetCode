public class MultiplyStrings {
    public String multiply(String num1, String num2) {
        char[] res = new char[num1.length() + num2.length()];
        for (int i = 0; i < res.length; i++) {
        	res[i] = '0';
        }
        int tmp = num1.length() + num2.length() - 2;
        for (int i = num1.length() - 1; i >= 0; i--) {
        	int carry = 0;
        	int val1 = num1.charAt(i) - '0';
        	for (int j = num2.length() - 1; j >= 0; j--) {
        		carry += (num2.charAt(j) - '0') * val1 + (res[tmp - i - j] - '0');
        		res[tmp - i - j] = (char) (carry % 10 + '0');
        		carry /= 10;
        	}
        	if (carry != 0) {
        		res[tmp - i + 1] = (char) (carry + '0');
        	}
        }
        tmp++;
        while (res[tmp] == '0' && tmp > 0) {
        	tmp--;
        }
        char[] ans = new char[tmp + 1];
        for (int i = 0; i < ans.length; i++) {
        	ans[i] = res[tmp - i];
        }
        return new String(ans);
    }
}