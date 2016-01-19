public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, ArrayList<Integer>> map = new HashMap<>();
        char[] arr;
        for (int i = 0; i < strs.length; i++) {
            arr = strs[i].toCharArray();
            Arrays.sort(arr);
            String key = new String(arr);
            if (map.containsKey(key)) {
                map.get(key).add(i);
            }
            else {
                ArrayList<Integer> list = new ArrayList<>();
                list.add(i);
                map.put(key, list);
            }
        }
        List<List<String>> res = new ArrayList<>();
        for (String k: map.keySet()) {
            ArrayList<String> group = new ArrayList<>();
            ArrayList<Integer> value = map.get(k);
            for (int i = 0; i < value.size(); i++) {
                group.add(strs[value.get(i)]);
            }
            Collections.sort(group);
            res.add(group);
        }
        return res;
    }
}
