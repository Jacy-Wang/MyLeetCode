public class Solution {
    public int calculate(String s) {
        StringBuilder ex = new StringBuilder();
        Stack<Character> stack = new Stack<>();
        char c;
        char top;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            if (Character.isDigit(c)) {
                ex.append(c);
            } else if (c == '(') {
                stack.push(c);
                ex.append(' ');
            } else if (c == ')') {
                top = stack.pop();
                while (top != '(') {
                    ex.append(top);
                    top = stack.pop();
                }
            } else if (c == '+' || c == '-') {
                while (!stack.empty()) {
                    top = stack.peek();
                    if (top == '(') {
                        stack.push(c);
                        break;
                    } else {
                        ex.append(top);
                        stack.pop();
                    }
                }
                if (stack.empty())
                    stack.push(c);
                ex.append(' ');
            }
        }
        while (!stack.empty()) {
            top = stack.pop();
            ex.append(top);
        }
        Stack<Integer> stack2 = new Stack<>();
        StringBuilder sb2 = new StringBuilder();
        int num1;
        int num2;
        for (int i = 0; i < ex.length(); i++) {
            c = ex.charAt(i);
            if (Character.isDigit(c)) {
                sb2.append(c);
            } else {
                if (sb2.length() > 0) {
                    stack2.push(Integer.parseInt(sb2.toString()));
                    sb2 = new StringBuilder();
                }
                if (c == '-' || c == '+') {
                    num1 = stack2.pop();
                    num2 = stack2.pop();
                    if (c == '-') {
                        stack2.push(num2 - num1);
                    } else {
                        stack2.push(num2 + num1);
                    }
                }
            }
        }
        return stack2.empty() ? Integer.parseInt(sb2.toString()) : stack2.pop();
    }
}
