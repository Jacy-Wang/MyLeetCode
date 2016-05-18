import java.util.Arrays;
import java.util.HashSet;
public class Solution {
    public String reverseVowels(String s) {
        int left = 0;
        int right = s.length() - 1;
        String vowel = "aeiouAEIOU";
        HashSet<Character> set = new HashSet<>(vowel.length());
        char[] arr = new char[s.length()];
        for (int i = 0; i < vowel.length(); i++) {
            set.add(vowel.charAt(i));
        }
        while (left < right) {
            if (!set.contains(s.charAt(left))) {
            	arr[left] = s.charAt(left);
                left++;
            }
            if (!set.contains(s.charAt(right))) {
            	arr[right] = s.charAt(right);
                right--;
            }
            if (set.contains(s.charAt(left)) && set.contains(s.charAt(right))) {
            	arr[left] = s.charAt(right);
            	arr[right] = s.charAt(left);
                left++;
                right--;
            }
        }
        if (left == right) {
        	arr[left] = s.charAt(left);
        }
        return new String(arr);
    }
}
