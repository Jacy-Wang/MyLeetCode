public class Solution {
    public String simplifyPath(String path) {
        StringBuilder sb = new StringBuilder();
        ArrayList<String> dirs = new ArrayList<>();
        path = path + '/';
        for (int i = 0; i < path.length(); i++) {
            
            if (path.charAt(i) == '/') {
                if (sb.length() == 0) {
                    continue;
                }
                else if (sb.toString().equals(".")) {
                    sb.delete(0, sb.length());
                }
                else if (sb.toString().equals("..")) {
                    sb.delete(0, sb.length());
                    if (dirs.size() > 0 ) {
                        dirs.remove(dirs.size() - 1);
                    }
                }
                else {
                    if (sb.length() > 0 ) {
                        dirs.add(sb.toString());
                        sb.delete(0, sb.length());
                    }
                }
            }
            else {
                sb.append(path.charAt(i));
            }
        }
        sb.delete(0, sb.length());
        for (String s : dirs) {
            sb.append('/');
            sb.append(s);
        }
        if (sb.length() == 0) {
            sb.append('/');
        }
        return sb.toString();
    }
}
