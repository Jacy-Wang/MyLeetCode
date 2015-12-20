public class StrStr {    
    public int strStr(String haystack, String needle) {
        if (needle.length() == 0) {
            return 0;
        }
        else if (haystack.length() == 0) {
            return -1;
        }
        for (int i = 0; i <= haystack.length() - needle.length(); i++) {
            if (haystack.charAt(i) == needle.charAt(0)) {
                if (haystack.substring(i + 1, i + needle.length()).equals(needle.substring(1))) {
                    return i;
                }
            }
        }
        return -1;
    }
}