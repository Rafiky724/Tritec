public class CountSmaller {
    public static int[] countSmaller(int[] nums) {
        int[] counts = new int[nums.length];
        
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[j] < nums[i]) {
                    counts[i]++;
                }
            }
        }
        
        return counts;
    }
}
        