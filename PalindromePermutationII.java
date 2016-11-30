import java.util.*;

public class PalindromePermutationII {
    public static void main(String[] args) {
        String s = args[0];
        ArrayList<String> res = new PalindromePermutationII().generatePalindromes(s);
        for (String r : res)
            System.out.println(r);
    }
    public ArrayList<String> generatePalindromes(String s) {
        ArrayList<String> lst = new ArrayList<>();
        HashMap<Character, Integer> map = new HashMap<>();
        int oddNum = canFormPalindrome(s, map);
        if (oddNum > 1)
            return lst;
        char oddChar = 'a';
        boolean hasOdd = false;
        StringBuilder half = new StringBuilder();
        for (Character c : map.keySet()) {
            int v = map.get(c);
            if ((v & 1) == 1) {
                oddChar = c;
                hasOdd = true;
            }
            for (int i = 0; i < v / 2; i++)
                half.append(c);
        }
        String halfS = half.toString();
        boolean[] visited = new boolean[halfS.length()];
        for (int i = 0; i < halfS.length(); i++)
            visited[i] = false;
        formPalindrome(halfS, new StringBuilder(), visited, lst);
        ArrayList<String> res = new ArrayList<>();
        for (String r : lst) {
            StringBuilder left = new StringBuilder(r);
            StringBuilder right = new StringBuilder(r);
            right.reverse();
            if (hasOdd)
                left.append(oddChar);
            res.add(left.append(right).toString());
        }
        return res;
    }

    public void formPalindrome(String s, StringBuilder sb, boolean[] visited, ArrayList<String> lst) {
        if (sb.length() == s.length()) {
            lst.add(sb.toString());
        } else {
            for (int i = 0; i < s.length(); i++) {
                if (!visited[i]) {
                    if (i > 0 && s.charAt(i) == s.charAt(i - 1) && visited[i - 1])
                        continue;
                     visited[i] = true;
                     sb.append(s.charAt(i));
                     formPalindrome(s, sb, visited, lst);
                     visited[i] = false;
                     sb.deleteCharAt(sb.length() - 1);
                }
            }
        }
    }

    public int canFormPalindrome(String s, HashMap<Character, Integer> map) {
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (map.containsKey(c)) {
                map.put(c, map.get(c) + 1);
            } else {
                map.put(c, 1);
            }
        }
        int oddNum = 0;
        for (Character c : map.keySet()) {
            if ((map.get(c) & 1) == 1)
                oddNum++;
        }
        return oddNum;
    }
}
