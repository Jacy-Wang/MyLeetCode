public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        Deque<String> queue = new ArrayDeque<>();
        int maxValidLen = 0;
        List<String> res = new ArrayList<>();
        Set<String> set = new HashSet<>();
        Set<String> candSet = new HashSet<>();
        queue.addLast(s);
        candSet.add(s);
        while (!queue.isEmpty()) {
            String top = queue.removeFirst();
            int len = isValid(top);
            if (len != -1) {
                if (maxValidLen == 0) {
                    maxValidLen = len;
                    set.add(top);
                } else {
                    if (len < maxValidLen)
                        break;
                    set.add(top);
                }
            } else {
                if (maxValidLen == 0) {
                    for (int i = 0; i < top.length(); i++) {
                        char c = top.charAt(i);
                        if (c == '(' || c == ')') {
                            String cand = top.substring(0, i) + top.substring(i + 1, top.length());
                            if (!candSet.contains(cand))
                                queue.addLast(cand);
                                candSet.add(cand);
                        }
                    }
                }
            }
        }
        Iterator<String> it = set.iterator();
        while (it.hasNext())
            res.add(it.next());
        return res;
    }
    
    private int isValid(String s) {
        Stack<Character> stack = new Stack<>();
        int len = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                stack.push(c);
                len++;
            } else if (c == ')') {
                if (stack.empty())
                    return -1;
                stack.pop();
            }
        }
        return stack.empty() ? len * 2 : -1;
    }
}
