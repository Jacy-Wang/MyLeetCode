import java.util.ArrayDeque;
import java.util.HashMap;

public class ValidParentheses {
    public boolean isValid(String s) {
        ArrayDeque<Character> deque = new ArrayDeque<>();
        HashMap<Character, Character> map = new HashMap<>();
        map.put(')', '(');
        map.put(']', '[');
        map.put('}', '{');
        for (int i = 0; i < s.length(); i++) {
        	char c = s.charAt(i);
        	if (c == '(' || c == '[' || c == '{') {
        		deque.addFirst(c);
        	}
        	else {
        		if (!deque.isEmpty()) {
            		char r = deque.removeFirst();
            		if (map.get(c) != r) {
            			return false;
            		}
        		}
        		else {
        			return false;
        		}
        	}
        }
        return deque.isEmpty();
    }
}