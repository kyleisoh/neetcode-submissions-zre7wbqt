class Solution {
    public boolean isAnagram(String s, String t) {
        int[] arr = new int[26];
        int[] empty_arr = new int[26];

        for (char ch : s.toCharArray()) {
            arr[(int) ch - 97] += 1;
        }

        for (char ch : t.toCharArray()) {
            arr[(int) ch - 97] -= 1;
        }
        System.out.println(Arrays.toString(arr));
        return Arrays.equals(arr, empty_arr);
    }
}
