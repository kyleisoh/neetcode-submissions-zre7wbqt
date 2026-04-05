class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        HashMap<Character, Integer> frequency = new HashMap<>();
        HashMap<Character, Integer> frequency2 = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            frequency.put(s.charAt(i), frequency.getOrDefault(s.charAt(i), 0) + 1);
            frequency2.put(t.charAt(i), frequency2.getOrDefault(t.charAt(i), 0) + 1);
        }

        return frequency.equals(frequency2);
    }
}
