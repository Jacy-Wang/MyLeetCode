public PalindromePermutation {
    public boolean canPermutePalindrome(String s) {
        HashMap<Character, Integer> map = new HashMap<>();
        for (char c : s) {
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
        return oddNum <= 1;
    }
}
