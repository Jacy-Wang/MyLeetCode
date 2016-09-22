public class Solution {
    public String decodeString(String s) {
        Deque<Character> stack = new ArrayDeque<>();
        StringBuilder sb = new StringBuilder();
        int counterL = 0;
        int counterR = 0;
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '[') {
                counterL++;
                stack.addFirst(ch);
            } else if (ch == ']') {
                counterR++;
                String cur = "";
                while (!stack.isEmpty()) {
                    char top = stack.removeFirst();
                    if (Character.isDigit(top)) {
                        String num = "";
                        num = top + num;
                        while (!stack.isEmpty()) {
                            char newTop = stack.removeFirst();
                            if (Character.isDigit(newTop)) {
                                num = newTop + num;
                            } else {
                                stack.addFirst(newTop);
                                break;
                            }
                        }
                        String tmp = String.join("", Collections.nCopies(Integer.parseInt(num), cur));
                        if (counterL == counterR) {
                            sb.append(tmp);
                        } else {
                            for (int j = 0; j < tmp.length(); j++) {
                                stack.addFirst(tmp.charAt(j));
                            }
                        }
                        break;
                    } else if (top == '[') {
                        continue;
                    } else {
                        cur = top + cur;
                    } 
                }
            } else if (Character.isDigit(ch)) {
                stack.addFirst(ch);
            } else {
                if (counterL == counterR)
                    sb.append(ch);
                else
                    stack.addFirst(ch);
            }
        }
        return sb.toString();
    }
}
