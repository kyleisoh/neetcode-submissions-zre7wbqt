class Solution {
    public boolean isAnagram(String s, String t) {
        int[] ordinance = new int[26];
        int[] ordinance2 = new int[26];

        if (s.length() != t.length()) {
            return false;
        }
        
        for (int i = 0; i < s.length(); i++) {
            int idx = (int) s.charAt(i) - (int) 'a';
            ordinance[idx] += 1;
            
            int idx2 = (int) t.charAt(i) - (int) 'a';
            ordinance2[idx2] += 1;
        }

        return Arrays.equals(ordinance, ordinance2);
    }
}
